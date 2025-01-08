from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from dependencies.logger import logger
from dependencies.constants import HomePageAPIConstants, HTTPStatus
from dependencies.utilities import Utilities
from dependencies.base_scraper import BaseScraper
from dependencies.models import WebsiteInput, WebsiteOutput

# Router instance
analysis_router = APIRouter()

api_helper = Utilities()
scraper_helper = BaseScraper()

@analysis_router.post(
    path="/homepage_analysis"
)

async def homepage_analysis_api(request: Request):
    try:
        body = await request.json()
        logger.info(f"body - {body}")

        # Request Authorization
        api_helper.authenticate(request.headers)

        # URL Validation
        input_data = WebsiteInput(**body)
        logger.info(f"input data - {input_data.url}")

        homepage_response = scraper_helper.make_webpage_request(input_data.url)

        if not homepage_response.status_code:
            raise InterruptedError("SOURCE_UNAVAILABLE")

        response_body = scraper_helper.get_response_analysis(homepage_response)

        logger.info(f"homepage analysis response: {response_body}")
        WebsiteOutput(**response_body)
        response_body.update({"http_response_code": HTTPStatus.OK})

    except InterruptedError as error:
        logger.error(f"Error Occurred - {error}")
        response_body = {
            "http_response_code": HomePageAPIConstants.ERROR_RESPONSES[str(error)][0],
            "error": HomePageAPIConstants.ERROR_RESPONSES[str(error)][1]
        }
    except Exception as error:
        logger.exception(f"Unexpected error Occurred - {error}")
        response_body = {
            "http_response_code": HomePageAPIConstants.ERROR_RESPONSES["INTERNAL_ERROR"][0],
            "error": HomePageAPIConstants.ERROR_RESPONSES["INTERNAL_ERROR"][1]
        }
    return JSONResponse(content=response_body, status_code=response_body["http_response_code"])


# @analysis_router.post(
#     "/analyze",
#     response_model=WebsiteOutput,
#     # dependencies=[Depends(authenticate)],
#     # status_code=status.HTTP_200_OK
# )
# async def analyze_website(input_data: WebsiteInput):
#     try:
#         response = requests.get(input_data.url, timeout=10)
#         response.raise_for_status()
#     except requests.RequestException as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=f"Error fetching the website: {str(e)}"
#         )
#
#     # Parse the website content
#     soup = BeautifulSoup(response.text, "html.parser")
#     text_content = soup.get_text(separator=" ").strip()
#
#     # Industry classification
#     candidate_labels = ["technology", "healthcare", "finance", "education", "retail"]
#     industry_result = industry_classifier(text_content, candidate_labels)
#     industry = industry_result["labels"][0] if industry_result["scores"][0] > 0.5 else None
#
#     # Company size and location analysis using OpenAI
#     prompt = (
#         f"Analyze the following text and provide answers for: Industry, Company Size, and Location.\n\n"
#         f"{text_content}\n\n"
#         f"Answers:"
#     )
#     try:
#         openai.api_key =
#         gpt_response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=prompt,
#             max_tokens=150
#         )
#         gpt_output = gpt_response.choices[0].text.strip().split("\n")
#         company_size = next((line.split(":")[1].strip() for line in gpt_output if "Company Size" in line), None)
#         location = next((line.split(":")[1].strip() for line in gpt_output if "Location" in line), None)
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error using GPT model: {str(e)}"
#         )
#
#     return WebsiteOutput(
#         industry=industry,
#         company_size=company_size,
#         location=location
#     )
