from fastapi import status


class HTTPStatus:
    OK = status.HTTP_200_OK
    UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
    BAD_REQUEST = status.HTTP_400_BAD_REQUEST
    INTERNAL_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR
    SOURCE_UNAVAILABLE = status.HTTP_503_SERVICE_UNAVAILABLE
    ENDPOINT_REQUEST_TIMED_OUT = status.HTTP_504_GATEWAY_TIMEOUT

class HomePageAPIConstants:
    ERROR_RESPONSES = {
        "NO_RECORD_FOUND": (status.HTTP_200_OK, "No Record Found for the given input", 103),
        "UNAUTHORIZED_ERROR": (status.HTTP_401_UNAUTHORIZED, "Authorization Incorrect or missing"),
        "BAD_INPUTS": (status.HTTP_400_BAD_REQUEST, "One or more input parameter is wrong or missing"),
        "INTERNAL_ERROR": (status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal error"),
        "SOURCE_UNAVAILABLE": (status.HTTP_503_SERVICE_UNAVAILABLE, "Source is busy or unavailable, Try again later"),
        "REQUEST_TIMEOUT": (status.HTTP_504_GATEWAY_TIMEOUT, "Endpoint Request Timed Out")
    }

    # Request Constants
    REQUEST_RETRY_COUNT = 3
    REQUEST_TIMEOUT = 10

    INDUSTRY_LABELS = ["technology", "healthcare", "finance", "education", "retail"]