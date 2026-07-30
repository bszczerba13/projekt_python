import os

"""
Central configuration for the test framework.

Values can be overridden using environment variables.
"""

TEST_ENVIRONMENT = os.getenv("TEST_ENVIRONMENT", "Local")

BASE_URL = os.getenv(
    "BASE_URL",
    "https://practicesoftwaretesting.com"
)

HEADLESS = os.getenv(
    "HEADLESS",
    "false"
).lower() == "true"