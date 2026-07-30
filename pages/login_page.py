import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.registration_page import RegistrationPage

class Locators:
    LOGIN_EMAIL = (By.ID, 'email')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-submit']")
    REGISTER_ACCOUNT_LINK = (By.CSS_SELECTOR, "[data-test='register-link']")
    LOGIN_PAGE_TITLE = (By.XPATH, "//h3[text()='Login']")
    INVALID_LOGIN_DATA_MESSAGE = (By.CSS_SELECTOR, "[data-test='login-error']")
    LOCKED_ACCOUNT_MESSAGE = (By.XPATH, "//div[contains(text(),'Account locked')]")

class LoginPage(BasePage):
    """
    Page object for login page.
    """

    @allure.step("Enter email")
    def enter_email(self, email):
        """
        Enter user email.
        """
        self.enter_text(Locators.LOGIN_EMAIL, email)

    @allure.step("Enter password")
    def enter_password(self, password):
        """
        Enter user password.
        """
        self.enter_text(Locators.LOGIN_PASSWORD, password)

    @allure.step("Click Login")
    def click_login_button(self):
        """
        Submit login form.
        """
        self.click(Locators.LOGIN_BUTTON)

    @allure.step("Open registration page")
    def click_register_link(self):
        """
        Open registration page.
        """
        self.click(Locators.REGISTER_ACCOUNT_LINK)
        return RegistrationPage(self.driver)

    def is_page_title_visible(self):
        """
        Return True if login page title is visible.
        """
        try:
            self.wait_for_visibility(Locators.LOGIN_PAGE_TITLE)
            return True
        except TimeoutException:
            return False

    def get_invalid_login_error(self):
        """
        Return invalid login error message.
        """
        return self.get_text(Locators.INVALID_LOGIN_DATA_MESSAGE)

    def is_account_locked(self):
        """
        Return True if user account is locked.
        """
        try:
            self.quick_wait_for_visibility(Locators.LOCKED_ACCOUNT_MESSAGE)
            return True
        except TimeoutException:
            return False

    def _verify_page(self):
        """
        Verify login page is loaded.
        """
        self.wait_for_visibility(Locators.LOGIN_EMAIL)