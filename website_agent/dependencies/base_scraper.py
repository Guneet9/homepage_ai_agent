import openai
import requests

from requests import Response
from bs4 import BeautifulSoup
from transformers import pipeline

from dependencies.logger import logger
from dependencies.configuration import Config
from dependencies.constants import HomePageAPIConstants, HTTPStatus

# Load AI models
industry_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

class BaseScraper:

    @staticmethod
    def make_webpage_request(url):
        response = Response()
        for _ in range(HomePageAPIConstants.REQUEST_RETRY_COUNT):
            try:
                response = requests.get(url=url, timeout=HomePageAPIConstants.REQUEST_TIMEOUT)
                logger.info(f"Response status code - {response.status_code}")
                if response.status_code == HTTPStatus.OK:
                    break
            except Exception as error:
                logger.exception(f"Error occurred while making request - {error}")
                continue
        return response

    @staticmethod
    def get_response_analysis(response):
        # Parse the website content
        soup = BeautifulSoup(response.text, "html.parser")
        text_content = soup.get_text(separator=" ").strip()

        # Industry classification
        industry_result = industry_classifier(text_content, HomePageAPIConstants.INDUSTRY_LABELS)
        industry = industry_result["labels"][0] if industry_result["scores"][0] > 0.5 else None

        logger.info(f"Industry - {industry}")

        # Company size and location analysis using OpenAI
        prompt = (
            f"Analyze the following text and provide answers for: Industry, Company Size, and Location.\n\n"
            f"{text_content}\n\n"
            f"Answers:"
        )

        try:
            openai.api_key = Config.OPEN_AI_AUTH_KEY
            gpt_response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )
            # Extracting details from the response
            gpt_output = gpt_response.choices[0].message['content'].strip().split("\n")
            company_size = next((line.split(":")[1].strip() for line in gpt_output if "Company Size" in line), None)
            location = next((line.split(":")[1].strip() for line in gpt_output if "Location" in line), None)
        except Exception as error:
            logger.exception(f"Error getting response from openai - {error}")
            raise InterruptedError("INTERNAL_ERROR")

        return {"industry": industry, "company_size": company_size, "location": location}
