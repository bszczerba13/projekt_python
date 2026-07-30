import platform
from pathlib import Path
import pytest
import selenium
from config import TEST_ENVIRONMENT

def create_environment_file(driver):
    environment_file = Path("allure-results/environment.properties")

    if environment_file.exists():
        return

    capabilities = driver.capabilities

    browser = capabilities.get("browserName", "Unknown").capitalize()
    browser_version = capabilities.get("browserVersion", "Unknown")

    os_name = f"{platform.system()} {platform.release()}"

    environment = {
        "Environment": TEST_ENVIRONMENT,
        "OS": os_name,
        "Python": platform.python_version(),
        "Pytest": pytest.__version__,
        "Selenium": selenium.__version__,
        "Browser": browser,
        "Browser.Version": browser_version,
    }

    with environment_file.open("w", encoding="utf-8") as file:
        for key, value in environment.items():
            file.write(f"{key}={value}\n")