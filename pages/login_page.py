from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.registration_page import RegistrationPage


class Locators:
    LOGIN_EMAIL = (By.ID, 'email')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-submit']")
    REGISTER_ACCOUNT_LINK = (By.CSS_SELECTOR, "[data-test='register-link']")

class LoginPage(BasePage):
    def enter_email(self, email):
        self.driver.find_element(*Locators.LOGIN_EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        return AccountPage(self.driver)

    def click_register_link(self):
        self.driver.find_element(*Locators.REGISTER_ACCOUNT_LINK).click()
        return RegistrationPage(self.driver)

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL))