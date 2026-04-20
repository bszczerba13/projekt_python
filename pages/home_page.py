from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage


class Locators:
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='nav-sign-in']")

class HomePage(BasePage):
    """
    Home Page Object
    """

    def click_sign_in(self):
        self.driver.find_element(*Locators.SIGN_IN_LINK).click()
        return LoginPage(self.driver)