from os import getenv

ALPHA_VANTAGE_BASE_URL = getenv(
    "ALPHA_VANTAGE_BASE_URL",
    default="https://www.alphavantage.co",
)
ALPHA_VANTAGE_API_KEY = getenv("ALPHA_VANTAGE_API_KEY")
