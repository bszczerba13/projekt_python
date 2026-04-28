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
    ORDER_STREET = (By.CSS_SELECTOR, "[data-test='street']")
    ORDER_CITY = (By.CSS_SELECTOR, "[data-test='city']")
    ORDER_STATE = (By.CSS_SELECTOR, "[data-test='state']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postal_code']")
    HOUSE_NUMBER = (By.CSS_SELECTOR, "[data-test='house_number']")
    AUTOFILL_LOADER = (By.CSS_SELECTOR, "[data-test='postcode-lookup-loading']")
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
    """
    Page object for checkout page.
    """

    def go_to_guest_tab(self):
        """
        Open guest checkout tab.
        """
        self.driver.find_element(*Locators.GUEST_TAB).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    def enter_guest_email(self, email):
        """
        Enter guest email.
        """
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)

    def enter_guest_first_name(self, first_name):
        """
        Enter guest first name.
        """
        self.driver.find_element(*Locators.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_guest_last_name(self, last_name):
        """
        Enter guest last name.
        """
        self.driver.find_element(*Locators.LAST_NAME_INPUT).send_keys(last_name)

    def click_continue_as_guest_button(self):
        """
        Continue checkout as guest.
        """
        self.driver.find_element(*Locators.CONTINUE_AS_GUEST_BUTTON).click()

    def get_guest_data_summary(self):
        """
        Return guest data summary.
        """
        guest_data_summary = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.GUEST_DATA_SUMMARY))
        return guest_data_summary.text

    def go_to_billing_address_step(self):
        """
        Proceed to billing address step.
        """
        self.driver.find_element(*Locators.PROCEED_TO_CHECKOUT_BUTTON_SIGN_IN_STEP).click()

    def select_guest_country(self):
        """
        Select guest random country.
        """
        self.select_random_option(Locators.COUNTRY_SELECT)

    def enter_postal_code(self, postal_code):
        """
        Enter guest postal code.
        """
        self.driver.find_element(*Locators.POSTAL_CODE).send_keys(postal_code)

    def enter_house_number(self, house_number):
        """
        Enter guest house number.
        """
        self.driver.find_element(*Locators.HOUSE_NUMBER).send_keys(house_number)

    def go_to_payment_step(self):
        """
        Proceed to payment step.
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.PROCEED_TO_CHECKOUT_BUTTON_BILLING_ADDRESS_STEP)).click()

    def choose_payment_method(self):
        """
        Choose payment method.
        """
        select = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PAYMENT_METHOD)))
        select.select_by_value("credit-card")

    def enter_card_number(self, card_number):
        """
        Enter credit card number.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CREDIT_CARD_NUMBER)).send_keys(card_number)

    def enter_card_expiration_date(self, card_expiration_date):
        """
        Enter credit card expiration date.
        """
        self.driver.find_element(*Locators.CARD_EXPIRATION_DATE).send_keys(card_expiration_date)

    def enter_card_cvv(self, card_cvv):
        """
        Enter credit card cvv number.
        """
        self.driver.find_element(*Locators.CARD_CVV_NUMBER).send_keys(card_cvv)

    def enter_card_holder_name(self, card_holder_name):
        """
        Enter credit card holder name.
        """
        self.driver.find_element(*Locators.CARD_HOLDER_NAME).send_keys(card_holder_name)

    def click_confirm_button(self):
        """
        Submit order confirmation.
        """
        self.driver.find_element(*Locators.CONFIRM_BUTTON).click()

    def get_payment_success_message(self):
        """
        Return payment success message.
        """
        payment_success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PAYMENT_SUCCESS_MESSAGE))
        return payment_success_message.text

    def get_order_confirmation_message(self):
        """
        Return order confirmation message.
        """
        order_confirmation_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_CONFIRMATION_MESSAGE))
        return order_confirmation_message.text

    def get_order_street(self):
        """
        Return autofilled street value.
        """
        order_street_value = self.driver.find_element(*Locators.ORDER_STREET).get_attribute("value")
        return order_street_value

    def get_order_city(self):
        """
        Return autofilled city value.
        """
        order_city_value = self.driver.find_element(*Locators.ORDER_CITY).get_attribute("value")
        return order_city_value

    def get_order_state(self):
        """
        Return autofilled state value.
        """
        order_state_value = self.driver.find_element(*Locators.ORDER_STATE).get_attribute("value")
        return order_state_value

    def wait_for_autofill(self):
        """
        Wait until autofill is completed.
        """
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(Locators.AUTOFILL_LOADER))

    def enter_order_street(self, order_street):
        """
        Enter order street.
        """
        self.driver.find_element(*Locators.ORDER_STREET).send_keys(order_street)

    def enter_order_city(self, order_city):
        """
        Enter order city.
        """
        self.driver.find_element(*Locators.ORDER_CITY).send_keys(order_city)

    def enter_order_state(self, order_state):
        """
        Enter order state.
        """
        self.driver.find_element(*Locators.ORDER_STATE).send_keys(order_state)

    def _verify_page(self):
        """
        Verify checkout page is loaded.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.GUEST_TAB))