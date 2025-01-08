import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    API_AUTH_KEY = os.getenv("SECRET_KEY")
    OPEN_AI_AUTH_KEY = os.getenv("OPENAI_API_KEY")
