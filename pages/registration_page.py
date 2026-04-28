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

class RegistrationPage(BasePage):
    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*Locators.LAST_NAME).send_keys(last_name)

    def enter_date_of_birth(self, date_of_birth):
        self.driver.find_element(*Locators.DATE_OF_BIRTH).send_keys(date_of_birth)

    def select_country(self):
        self.select_random_option(Locators.COUNTRY)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*Locators.POSTAL_CODE).send_keys(postal_code)

    def enter_house_number(self, house_number):
        self.driver.find_element(*Locators.HOUSE_NUMBER).send_keys(house_number)

    def enter_phone(self, phone):
        self.driver.find_element(*Locators.PHONE).send_keys(phone)

    def enter_registration_email(self, email):
        self.driver.find_element(*Locators.EMAIL).send_keys(email)

    def enter_registration_password(self, password):
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_register_button(self):
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()

    def get_street_value(self):
        street_value = self.driver.find_element(*Locators.STREET).get_attribute("value")
        return street_value

    def get_city_value(self):
        city_value = self.driver.find_element(*Locators.CITY).get_attribute("value")
        return city_value

    def get_state_value(self):
        state_value = self.driver.find_element(*Locators.STATE).get_attribute("value")
        return state_value

    def enter_street(self, street):
        self.driver.find_element(*Locators.STREET).send_keys(street)

    def enter_city(self, city):
        self.driver.find_element(*Locators.CITY).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(*Locators.STATE).send_keys(state)

    def wait_for_autofill_loader(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(Locators.AUTOFILL_LOADER))

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.FIRST_NAME))