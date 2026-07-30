import allure
import pytest
from selenium import webdriver
import config
from pages.home_page import HomePage
from utils.data_generator import DataGenerator
from selenium.webdriver.chrome.options import Options
from utils.environment import create_environment_file

@pytest.fixture
def driver(request):
    """
    Create browser instance and open application.
    """
    options = Options()

    if config.HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    request.node.driver = driver
    create_environment_file(driver)
    driver.get(config.BASE_URL)

    yield driver

    driver.quit()

@pytest.fixture
def home_page(driver):
    """
    Return home page object.
    """
    return HomePage(driver)

@pytest.fixture
def product_page(home_page):
    """
    Open product page.
    """
    return home_page.open_first_available_product()

@pytest.fixture
def login_page(home_page):
    """
    Open login page.
    """
    return home_page.header.click_sign_in()

@pytest.fixture
def registration_page(login_page):
    """
    Open registration page.
    """
    return login_page.click_register_link()

@pytest.fixture
def data_generator():
    """
    Return test data generator instance.
    """
    return DataGenerator()

@pytest.fixture
def registration_data(data_generator):
    """
    Generate registration test data.
    """
    return data_generator.registration_data_generator()

@pytest.fixture
def order_data(data_generator):
    """
    Generate checkout order data.
    """
    return data_generator.order_data_generator()

@pytest.fixture
def invalid_login_data(data_generator):
    """
    Generate invalid login credentials.
    """
    return data_generator.invalid_login_data_generator()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Screenshot ({report.when})",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as error:
                print(f"Warning: Unable to attach screenshot: {error}")