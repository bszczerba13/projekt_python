import allure
from selenium.webdriver.common.by import By
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

    @allure.step("Open guest checkout")
    def go_to_guest_tab(self):
        """
        Open guest checkout tab.
        """
        self.click(Locators.GUEST_TAB)

    @allure.step("Enter email")
    def enter_guest_email(self, email):
        """
        Enter guest email.
        """
        self.enter_text(Locators.EMAIL_INPUT, email)

    @allure.step("Enter first name")
    def enter_guest_first_name(self, first_name):
        """
        Enter guest first name.
        """
        self.enter_text(Locators.FIRST_NAME_INPUT, first_name)

    @allure.step("Enter last name")
    def enter_guest_last_name(self, last_name):
        """
        Enter guest last name.
        """
        self.enter_text(Locators.LAST_NAME_INPUT, last_name)

    @allure.step("Continue as guest")
    def click_continue_as_guest_button(self):
        """
        Continue checkout as guest.
        """
        self.click(Locators.CONTINUE_AS_GUEST_BUTTON)

    def get_guest_data_summary(self):
        """
        Return guest data summary.
        """
        return self.get_text(Locators.GUEST_DATA_SUMMARY)

    @allure.step("Proceed to billing address")
    def go_to_billing_address_step(self):
        """
        Proceed to billing address step.
        """
        self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON_SIGN_IN_STEP)

    @allure.step("Select country")
    def select_guest_country(self):
        """
        Select guest random country.
        """
        self.select_random_option(Locators.COUNTRY_SELECT)

    @allure.step("Enter postal code")
    def enter_postal_code(self, postal_code):
        """
        Enter guest postal code.
        """
        self.enter_text(Locators.POSTAL_CODE, postal_code)

    @allure.step("Enter house number")
    def enter_house_number(self, house_number):
        """
        Enter guest house number.
        """
        self.enter_text(Locators.HOUSE_NUMBER, house_number)

    @allure.step("Proceed to payment")
    def go_to_payment_step(self):
        """
        Proceed to payment step.
        """
        self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON_BILLING_ADDRESS_STEP)

    @allure.step("Choose payment method")
    def choose_payment_method(self, payment_method):
        """
        Choose payment method.
        """
        self.select_by_value(Locators.PAYMENT_METHOD, payment_method)

    @allure.step("Enter card number")
    def enter_card_number(self, card_number):
        """
        Enter credit card number.
        """
        self.enter_text(Locators.CREDIT_CARD_NUMBER, card_number)

    @allure.step("Enter card expiration date")
    def enter_card_expiration_date(self, card_expiration_date):
        """
        Enter credit card expiration date.
        """
        self.enter_text(Locators.CARD_EXPIRATION_DATE, card_expiration_date)

    @allure.step("Enter card CVV")
    def enter_card_cvv(self, card_cvv):
        """
        Enter credit card cvv number.
        """
        self.enter_text(Locators.CARD_CVV_NUMBER, card_cvv)

    @allure.step("Enter card holder name")
    def enter_card_holder_name(self, card_holder_name):
        """
        Enter credit card holder name.
        """
        self.enter_text(Locators.CARD_HOLDER_NAME, card_holder_name)

    @allure.step("Confirm order")
    def click_confirm_button(self):
        """
        Submit order confirmation.
        """
        self.click(Locators.CONFIRM_BUTTON)

    def get_payment_success_message(self):
        """
        Return payment success message.
        """
        return self.get_text(Locators.PAYMENT_SUCCESS_MESSAGE)

    def get_order_confirmation_message(self):
        """
        Return order confirmation message.
        """
        return self.get_text(Locators.ORDER_CONFIRMATION_MESSAGE)

    def get_order_street(self):
        """
        Return autofilled street value.
        """
        return self.get_element_attribute(Locators.ORDER_STREET, "value")

    def get_order_city(self):
        """
        Return autofilled city value.
        """
        return self.get_element_attribute(Locators.ORDER_CITY, "value")

    def get_order_state(self):
        """
        Return autofilled state value.
        """
        return self.get_element_attribute(Locators.ORDER_STATE, "value")

    def wait_for_autofill(self):
        """
        Wait until autofill is completed.
        """
        self.wait_for_invisibility(Locators.AUTOFILL_LOADER)

    @allure.step("Enter street")
    def enter_order_street(self, order_street):
        """
        Enter order street.
        """
        self.enter_text(Locators.ORDER_STREET, order_street)

    @allure.step("Enter city")
    def enter_order_city(self, order_city):
        """
        Enter order city.
        """
        self.enter_text(Locators.ORDER_CITY, order_city)

    @allure.step("Enter state")
    def enter_order_state(self, order_state):
        """
        Enter order state.
        """
        self.enter_text(Locators.ORDER_STATE, order_state)

    def _verify_page(self):
        """
        Verify checkout page is loaded.
        """
        self.wait_for_visibility(Locators.GUEST_TAB)