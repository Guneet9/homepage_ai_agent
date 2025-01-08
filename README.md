# FastAPI AI Agent for Website Scraping

## Overview
This application uses AI to analyze the homepage of a website and extracts details about:
- Industry
- Company Size
- Location

## Features
- Secure with secret key-based authentication
- AI-powered analysis using Transformers and OpenAI GPT
- Modular, scalable code structure

## Setup

### Prerequisites
- Python 3.10 or above
- Install all the required packages using pip install -r requirements.txt

### Access the Project
- Run the project locally using the command uvicorn main:app --reload
- Access the project by making a POST request to url http://127.0.0.1:8000/analysis/homepage_analysis
- Add Authorization "123456" in headers before making the request
