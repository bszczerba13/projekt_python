from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class Locators:
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='page-title']")

class AccountPage(BasePage):
    def get_page_title(self):
        return self.driver.find_element(*Locators.PAGE_TITLE).text

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PAGE_TITLE))
