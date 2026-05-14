from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Locators:
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='page-title']")

class AccountPage(BasePage):
    """
    Page object for account page.
    """
    def get_page_title(self):
        """
        Return account page title.
        """
        return self.get_text(Locators.PAGE_TITLE)

    def _verify_page(self):
        """
        Verify account page is loaded.
        """
        self.wait_for_visibility(Locators.PAGE_TITLE)