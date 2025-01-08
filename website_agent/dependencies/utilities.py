from fastapi import Header
from dependencies.configuration import Config
from dependencies.logger import logger


class Utilities:
    @staticmethod
    def authenticate(headers: Header()) -> None:
        logger.info(f"Headers received - {headers}")
        auth_token = headers.get("authorization")
        logger.info(f"Auth Token - {auth_token} | {Config.API_AUTH_KEY}")
        if not auth_token or auth_token != Config.API_AUTH_KEY:
            raise InterruptedError("UNAUTHORIZED_ERROR")
