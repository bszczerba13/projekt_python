import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import DEFAULT_TIMEOUT, QUICK_TIMEOUT


class BasePage:
    """
    Base Page Object for all pages.
    """
    def __init__(self, driver):
        """
        Initialize page object and verify page.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
        self.quick_wait = WebDriverWait(driver, QUICK_TIMEOUT)
        self._verify_page()

    def _verify_page(self):
        """
        Verify current page.
        """
        return

    def wait_for_visibility(self, locator):
        """
        Wait until element is visible.
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """
        Wait until element is clickable.
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_invisibility(self, locator):
        """
        Wait until element disappears.
        """
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_presence(self, locator):
        """
        Wait until element is present.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def enter_text(self, locator, text):
        """
        Enter text into element.
        """
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        """
        Click element.
        """
        self.wait_for_clickable(locator).click()

    def get_text(self, locator):
        """
        Return element text.
        """
        return self.wait_for_visibility(locator).text

    def quick_wait_for_visibility(self, locator):
        """
        Wait until element is visible.
        """
        return self.quick_wait.until(EC.visibility_of_element_located(locator))

    def get_element_attribute(self, locator, attribute):
        """
        Return element attribute value.
        """
        return self.wait_for_visibility(locator).get_attribute(attribute)

    def get_elements(self, locator):
        """
        Return list of web elements.
        """
        return self.driver.find_elements(*locator)

    def select_random_option(self, locator):
        """
        Select a random option from dropdown.
        Limited range is used intentionally to avoid
        loading large dropdown lists (e.g. country list).
        """
        select = Select(self.wait_for_visibility(locator))
        index = random.randint(1, 20)
        select.select_by_index(index)

    def select_by_value(self, locator, value):
        """
        Select by value from dropdown.
        """
        select = Select(self.wait_for_visibility(locator))
        select.select_by_value(value)