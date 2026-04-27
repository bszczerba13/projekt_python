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
        list_options = select.options
        index = random.randint(1, len(list_options) - 1)
        select.select_by_index(index)