from tests.base_test import BaseTest
from utils.data_generator import DataGenerator

class TestCheckout(BaseTest):
    """
    Checkout test cases.
    """
    def setUp(self):
        """
         Set up for checkout test.
        """
        super().setUp()
        self.product_page = self.home_page.open_first_available_product()
        self.order_data = DataGenerator().order_data_generator()

    def test_checkout(self):
        """
        Verify guest checkout flow.
        """
        self.product_page.add_product_to_cart()
        self.cart_page = self.product_page.go_to_cart()
        self.checkout_page = self.cart_page.go_to_checkout()
        self.checkout_page.go_to_guest_tab()
        self.checkout_page.enter_guest_email(self.order_data["email_address"])
        self.checkout_page.enter_guest_first_name(self.order_data["first_name"])
        self.checkout_page.enter_guest_last_name(self.order_data["last_name"])
        self.checkout_page.click_continue_as_guest_button()
        guest_data = self.checkout_page.get_guest_data_summary()
        self.assertIn(self.order_data["email_address"], guest_data)
        self.assertIn(self.order_data["first_name"], guest_data)
        self.assertIn(self.order_data["last_name"], guest_data)
        self.checkout_page.go_to_billing_address_step()
        self.checkout_page.select_guest_country()
        self.checkout_page.enter_postal_code(self.order_data["postal_code"])
        self.checkout_page.enter_house_number(self.order_data["house_number"])
        self.checkout_page.wait_for_autofill()
        if self.checkout_page.get_order_street() == "":
            self.checkout_page.enter_order_street(self.order_data["street"])
        if self.checkout_page.get_order_city() == "":
            self.checkout_page.enter_order_city(self.order_data["city"])
        if self.checkout_page.get_order_state() == "":
            self.checkout_page.enter_order_state(self.order_data["state"])
        self.checkout_page.go_to_payment_step()
        self.checkout_page.choose_payment_method()
        self.checkout_page.enter_card_number(self.order_data["credit_card_number"])
        self.checkout_page.enter_card_expiration_date(self.order_data["card_expiration_date"])
        self.checkout_page.enter_card_cvv(self.order_data["card_cvv"])
        self.checkout_page.enter_card_holder_name(f"{self.order_data['first_name']} {self.order_data['last_name']}")
        self.checkout_page.click_confirm_button()
        payment_success_message = self.checkout_page.get_payment_success_message().lower()
        self.assertIn("success", payment_success_message)
        self.checkout_page.click_confirm_button()
        order_confirmation_message = self.checkout_page.get_order_confirmation_message().lower()
        self.assertIn("your invoice number", order_confirmation_message)