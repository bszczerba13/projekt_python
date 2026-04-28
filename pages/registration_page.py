from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        Enter last name.
        """
        self.driver.find_element(*Locators.LAST_NAME).send_keys(last_name)

    def enter_date_of_birth(self, date_of_birth):
        """
        Enter date of birth.
        """
        self.driver.find_element(*Locators.DATE_OF_BIRTH).send_keys(date_of_birth)

    def select_country(self):
        """
        Select random country.
        """
        self.select_random_option(Locators.COUNTRY)

    def enter_postal_code(self, postal_code):
        """
        Enter postal code.
        """
        self.driver.find_element(*Locators.POSTAL_CODE).send_keys(postal_code)

    def enter_house_number(self, house_number):
        """
        Enter house number.
        """
        self.driver.find_element(*Locators.HOUSE_NUMBER).send_keys(house_number)

    def enter_phone(self, phone):
        """
        Enter phone number.
        """
        self.driver.find_element(*Locators.PHONE).send_keys(phone)

    def enter_registration_email(self, email):
        """
        Enter email address.
        """
        self.driver.find_element(*Locators.EMAIL).send_keys(email)

    def enter_registration_password(self, password):
        """
        Enter password.
        """
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_register_button(self):
        """
        Submit registration form.
        """
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()

    def get_street_value(self):
        """
        Return autofilled street value.
        """
        street_value = self.driver.find_element(*Locators.STREET).get_attribute("value")
        return street_value

    def get_city_value(self):
        """
        Return autofilled city value.
        """
        city_value = self.driver.find_element(*Locators.CITY).get_attribute("value")
        return city_value

    def get_state_value(self):
        """
        Return autofilled state value.
        """
        state_value = self.driver.find_element(*Locators.STATE).get_attribute("value")
        return state_value

    def enter_street(self, street):
        """
        Enter street.
        """
        self.driver.find_element(*Locators.STREET).send_keys(street)

    def enter_city(self, city):
        """
        Enter city.
        """
        self.driver.find_element(*Locators.CITY).send_keys(city)

    def enter_state(self, state):
        """
        Enter state.
        """
        self.driver.find_element(*Locators.STATE).send_keys(state)

    def wait_for_autofill_loader(self):
        """
        Wait until autofill is completed.
        """
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(Locators.AUTOFILL_LOADER))

    def get_missing_email_error_message(self):
        """
        Return missing email validation message.
        """
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.MISSING_EMAIL_MESSAGE)).text
        return error_message

    def _verify_page(self):
        """
        Verify registration page is loaded.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.FIRST_NAME))