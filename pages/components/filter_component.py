import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Locators:
    FILTERING_COMPLETED = (By.CSS_SELECTOR, "[data-test='filter_completed']")

class FilterComponent(BasePage):
    """
    Product filtering component.
    """

    @allure.step("Filter products by: {category}")
    def filter_by_category(self, category):
        """
        Filter products by category.
        """
        locator = (By.XPATH, f"//label[contains(text(), '{category}')]")
        self.click(locator)
        self.wait_for_presence(Locators.FILTERING_COMPLETED)