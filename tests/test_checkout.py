from tests.base_test import BaseTest
from utils.data_generator import OrderDataGenerator

class TestCheckout(BaseTest):
    def setUp(self):
        super().setUp()
        self.product_page = self.home_page.open_first_available_product()
        self.data = OrderDataGenerator()

    def test_checkout(self):

        self.product_page.add_product_to_cart()
        self.cart_page = self.product_page.go_to_cart()
        self.checkout_page = self.cart_page.go_to_checkout()
        self.checkout_page.go_to_guest_tab()
        self.checkout_page.enter_guest_email(self.data.EMAIL)
        self.checkout_page.enter_guest_first_name(self.data.FIRST_NAME)
        self.checkout_page.enter_guest_last_name(self.data.LAST_NAME)
        self.checkout_page.click_continue_as_guest_button()
        guest_data = self.checkout_page.get_guest_data_summary()
        self.assertIn(self.data.EMAIL, guest_data)
        self.assertIn(self.data.FIRST_NAME, guest_data)
        self.assertIn(self.data.LAST_NAME, guest_data)
        self.checkout_page.go_to_billing_address_step()
        self.checkout_page.select_guest_country()
        self.checkout_page.enter_postal_code(self.data.POSTAL_CODE)
        self.checkout_page.enter_house_number(self.data.HOUSE_NUMBER)
        self.checkout_page.wait_for_autofill()
        if self.checkout_page.get_order_street() == "":
            self.checkout_page.enter_order_street(self.data.STREET)
        if self.checkout_page.get_order_city() == "":
            self.checkout_page.enter_order_city(self.data.CITY)
        if self.checkout_page.get_order_state() == "":
            self.checkout_page.enter_order_state(self.data.STATE)
        self.checkout_page.go_to_payment_step()
        self.checkout_page.choose_payment_method()
        self.checkout_page.enter_card_number(self.data.CREDIT_CARD_NUMBER)
        self.checkout_page.enter_card_expiration_date(self.data.CARD_EXPIRATION_DATE)
        self.checkout_page.enter_card_cvv(self.data.CARD_CVV)
        self.checkout_page.enter_card_holder_name(f"{self.data.FIRST_NAME} {self.data.LAST_NAME}")
        self.checkout_page.click_confirm_button()
        payment_success_message = self.checkout_page.get_payment_success_message().lower()
        self.assertIn("success", payment_success_message)
        self.checkout_page.click_confirm_button()
        order_confirmation_message = self.checkout_page.get_order_confirmation_message().lower()
        self.assertIn("your invoice number", order_confirmation_message)