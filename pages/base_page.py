import random
from selenium.webdriver.support.select import Select


class BasePage:
    """
    Base Page Object for all pages
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        return

    def select_random_option(self, locator):
        dropdown_list = self.driver.find_element(*locator)
        select = Select(dropdown_list)
        index = random.randint(1, 20)
        select.select_by_index(index)