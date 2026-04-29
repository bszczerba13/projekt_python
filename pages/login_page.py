from selenium.common import TimeoutException
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
    LOGIN_PAGE_TITLE = (By.XPATH, "//h3[text()='Login']")
    INVALID_LOGIN_DATA_MESSAGE = (By.CSS_SELECTOR, "[data-test='login-error']")
    LOCKED_ACCOUNT_MESSAGE = (By.XPATH, "//div[contains(text(),'Account locked')]")

class LoginPage(BasePage):
    """
    Page object for login page.
    """
    def enter_email(self, email):
        """
        Enter user email.
        """
        self.driver.find_element(*Locators.LOGIN_EMAIL).send_keys(email)

    def enter_password(self, password):
        """
        Enter user password.
        """
        self.driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)

    def click_login_button(self):
        """
        Submit login form.
        """
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

    def click_register_link(self):
        """
        Open registration page.
        """
        self.driver.find_element(*Locators.REGISTER_ACCOUNT_LINK).click()
        return RegistrationPage(self.driver)

    def is_page_title_visible(self):
        """
        Return True if login page title is visible.
        """
        login_page_title = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE))
        return login_page_title.is_displayed()

    def get_invalid_login_error(self):
        """
        Return invalid login error message.
        """
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.INVALID_LOGIN_DATA_MESSAGE)).text
        return error_message

    def is_account_locked(self):
        """
        Return True if user account is locked.
        """
        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(Locators.LOCKED_ACCOUNT_MESSAGE))
            return True
        except TimeoutException:
            return False

    def _verify_page(self):
        """
        Verify login page is loaded.
        """
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL))