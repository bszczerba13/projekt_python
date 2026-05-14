from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Locators:
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='first-name']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='last-name']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "[data-test='dob']")
    COUNTRY = (By.CSS_SELECTOR, "[data-test='country']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postal_code']")
    HOUSE_NUMBER = (By.CSS_SELECTOR, "[data-test='house_number']")
    STREET = (By.CSS_SELECTOR, "[data-test='street']")
    CITY = (By.CSS_SELECTOR, "[data-test='city']")
    STATE = (By.CSS_SELECTOR, "[data-test='state']")
    PHONE = (By.CSS_SELECTOR, "[data-test='phone']")
    EMAIL = (By.CSS_SELECTOR, "[data-test='email']")
    PASSWORD = (By.CSS_SELECTOR, "[data-test='password']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[data-test='register-submit']")
    AUTOFILL_LOADER = (By.CSS_SELECTOR, "[data-test='postcode-lookup-loading']")
    MISSING_EMAIL_MESSAGE = (By.CSS_SELECTOR, "[data-test='email-error']")

class RegistrationPage(BasePage):
    """
    Page object for registration page.
    """
    def enter_first_name(self, first_name):
        """
        Enter first name.
        """
        self.enter_text(Locators.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        """
        Enter last name.
        """
        self.enter_text(Locators.LAST_NAME, last_name)

    def enter_date_of_birth(self, date_of_birth):
        """
        Enter date of birth.
        """
        self.enter_text(Locators.DATE_OF_BIRTH, date_of_birth)

    def select_country(self):
        """
        Select random country.
        """
        self.select_random_option(Locators.COUNTRY)

    def enter_postal_code(self, postal_code):
        """
        Enter postal code.
        """
        self.enter_text(Locators.POSTAL_CODE, postal_code)

    def enter_house_number(self, house_number):
        """
        Enter house number.
        """
        self.enter_text(Locators.HOUSE_NUMBER, house_number)

    def enter_phone(self, phone):
        """
        Enter phone number.
        """
        self.enter_text(Locators.PHONE, phone)

    def enter_registration_email(self, email):
        """
        Enter email address.
        """
        self.enter_text(Locators.EMAIL, email)

    def enter_registration_password(self, password):
        """
        Enter password.
        """
        self.enter_text(Locators.PASSWORD, password)

    def click_register_button(self):
        """
        Submit registration form.
        """
        self.click(Locators.REGISTER_BUTTON)

    def get_street_value(self):
        """
        Return autofilled street value.
        """
        return self.get_element_attribute(Locators.STREET, "value")

    def get_city_value(self):
        """
        Return autofilled city value.
        """
        return self.get_element_attribute(Locators.CITY, "value")

    def get_state_value(self):
        """
        Return autofilled state value.
        """
        return self.get_element_attribute(Locators.STATE, "value")

    def enter_street(self, street):
        """
        Enter street.
        """
        self.enter_text(Locators.STREET, street)

    def enter_city(self, city):
        """
        Enter city.
        """
        self.enter_text(Locators.CITY, city)

    def enter_state(self, state):
        """
        Enter state.
        """
        self.enter_text(Locators.STATE, state)

    def wait_for_autofill_loader(self):
        """
        Wait until autofill is completed.
        """
        self.wait_for_invisibility(Locators.AUTOFILL_LOADER)

    def get_missing_email_error_message(self):
        """
        Return missing email validation message.
        """
        return self.get_text(Locators.MISSING_EMAIL_MESSAGE)

    def _verify_page(self):
        """
        Verify registration page is loaded.
        """
        self.wait_for_visibility(Locators.FIRST_NAME)