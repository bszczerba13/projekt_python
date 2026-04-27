from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Locators:
    GUEST_TAB = (By.CSS_SELECTOR, "a[href='#guest-tab']")
    EMAIL_INPUT = (By.ID, "guest-email")
    FIRST_NAME_INPUT = (By.ID, "guest-first-name")
    LAST_NAME_INPUT = (By.ID, "guest-last-name")
    CONTINUE_AS_GUEST_BUTTON = (By.CSS_SELECTOR, "[data-test='guest-submit']")
    GUEST_DATA_SUMMARY = (By.XPATH, "//p[contains(text(), 'Continuing as guest')]")
    PROCEED_TO_CHECKOUT_BUTTON_SIGN_IN_STEP = (By.CSS_SELECTOR, "[data-test='proceed-2-guest']")
    COUNTRY_SELECT = (By.CSS_SELECTOR, "[data-test='country']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postal_code']")
    HOUSE_NUMBER = (By.CSS_SELECTOR, "[data-test='house_number']")
    PROCEED_TO_CHECKOUT_BUTTON_BILLING_ADDRESS_STEP = (By.CSS_SELECTOR, "[data-test='proceed-3']")
    PAYMENT_METHOD = (By.CSS_SELECTOR, "[data-test='payment-method']")
    CREDIT_CARD_NUMBER = (By.CSS_SELECTOR, "[data-test='credit_card_number']")
    CARD_EXPIRATION_DATE = (By.CSS_SELECTOR, "[data-test='expiration_date']")
    CARD_CVV_NUMBER = (By.CSS_SELECTOR, "[data-test='cvv']")
    CARD_HOLDER_NAME = (By.CSS_SELECTOR, "[data-test='card_holder_name']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    PAYMENT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-test='payment-success-message']")
    ORDER_CONFIRMATION_MESSAGE = (By.ID, "order-confirmation")

class CheckoutPage(BasePage):

    def go_to_guest_tab(self):
        self.driver.find_element(*Locators.GUEST_TAB).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    def enter_guest_email(self, email):
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)

    def enter_guest_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_guest_last_name(self, last_name):
        self.driver.find_element(*Locators.LAST_NAME_INPUT).send_keys(last_name)

    def click_continue_as_guest_button(self):
        self.driver.find_element(*Locators.CONTINUE_AS_GUEST_BUTTON).click()

    def get_guest_data_summary(self):
        guest_data_summary = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.GUEST_DATA_SUMMARY))
        return guest_data_summary.text

    def go_to_billing_address_step(self):
        self.driver.find_element(*Locators.PROCEED_TO_CHECKOUT_BUTTON_SIGN_IN_STEP).click()

    def select_guest_country(self):
        self.select_random_option(Locators.COUNTRY_SELECT)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*Locators.POSTAL_CODE).send_keys(postal_code)

    def enter_house_number(self, house_number):
        self.driver.find_element(*Locators.HOUSE_NUMBER).send_keys(house_number)

    def go_to_payment_step(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.PROCEED_TO_CHECKOUT_BUTTON_BILLING_ADDRESS_STEP)).click()

    def choose_payment_method(self):
        select = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PAYMENT_METHOD)))
        select.select_by_value("credit-card")

    def enter_card_number(self, card_number):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CREDIT_CARD_NUMBER)).send_keys(card_number)

    def enter_card_expiration_date(self, card_expiration_date):
        self.driver.find_element(*Locators.CARD_EXPIRATION_DATE).send_keys(card_expiration_date)

    def enter_card_cvv(self, card_cvv):
        self.driver.find_element(*Locators.CARD_CVV_NUMBER).send_keys(card_cvv)

    def enter_card_holder_name(self, card_holder_name):
        self.driver.find_element(*Locators.CARD_HOLDER_NAME).send_keys(card_holder_name)

    def click_confirm_button(self):
        self.driver.find_element(*Locators.CONFIRM_BUTTON).click()

    def get_payment_success_message(self):
        payment_success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PAYMENT_SUCCESS_MESSAGE))
        return payment_success_message.text

    def get_order_confirmation_message(self):
        order_confirmation_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_CONFIRMATION_MESSAGE))
        return order_confirmation_message.text

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.GUEST_TAB))