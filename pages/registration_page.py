from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
import random

class Locators:
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='first-name']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='last-name']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "[data-test='dob']")
    COUNTRY = (By.CSS_SELECTOR, "[data-test='country']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postal_code']")
    HOUSE_NUMBER = (By.CSS_SELECTOR, "[data-test='house_number']")
    PHONE = (By.CSS_SELECTOR, "[data-test='phone']")
    EMAIL = (By.CSS_SELECTOR, "[data-test='email']")
    PASSWORD = (By.CSS_SELECTOR, "[data-test='password']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[data-test='register-submit']")

class RegistrationPage(BasePage):
    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*Locators.LAST_NAME).send_keys(last_name)

    def enter_date_of_birth(self, date_of_birth):
        self.driver.find_element(*Locators.DATE_OF_BIRTH).send_keys(date_of_birth)

    def select_country(self):
        countries_list = self.driver.find_element(*Locators.COUNTRY)
        select = Select(countries_list)
        countries = select.options
        index = random.randint(1, len(countries)-1)
        select.select_by_index(index)

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

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.FIRST_NAME))