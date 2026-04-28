from utils.data_generator import DataGenerator
from tests.base_test import BaseTest

class RegistrationTest(BaseTest):
    """
    Registration test cases.
    """
    def setUp(self):
        """
        Set up registration test data.
        """
        super().setUp()
        self.login_page = self.home_page.click_sign_in()
        self.registration_page = self.login_page.click_register_link()
        self.registration_data = DataGenerator().registration_data_generator()

    def test_registration(self):
        """
        Verify successful user registration.
        """
        self.registration_page.enter_first_name(self.registration_data["first_name"])
        self.registration_page.enter_last_name(self.registration_data["last_name"])
        self.registration_page.enter_date_of_birth(self.registration_data["date_of_birth"])
        self.registration_page.select_country()
        self.registration_page.enter_postal_code(self.registration_data["postal_code"])
        self.registration_page.enter_house_number(self.registration_data["house_number"])
        self.registration_page.enter_phone(self.registration_data["phone_number"])
        self.registration_page.enter_registration_email(self.registration_data["email_address"])
        self.registration_page.enter_registration_password(self.registration_data["password"])
        self.registration_page.wait_for_autofill_loader()
        if self.registration_page.get_street_value() == "":
            self.registration_page.enter_street(self.registration_data["street"])
        if self.registration_page.get_city_value() == "":
            self.registration_page.enter_city(self.registration_data["city"])
        if self.registration_page.get_state_value() == "":
            self.registration_page.enter_state(self.registration_data["state"])
        self.registration_page.click_register_button()
        self.assertTrue(self.login_page.is_page_title_visible())

    def test_registration_missing_email(self):
        """
        Verify registration validation when email is missing.
        """
        self.registration_page.enter_first_name(self.registration_data["first_name"])
        self.registration_page.enter_last_name(self.registration_data["last_name"])
        self.registration_page.enter_date_of_birth(self.registration_data["date_of_birth"])
        self.registration_page.select_country()
        self.registration_page.enter_postal_code(self.registration_data["postal_code"])
        self.registration_page.enter_house_number(self.registration_data["house_number"])
        self.registration_page.enter_phone(self.registration_data["phone_number"])
        self.registration_page.enter_registration_password(self.registration_data["password"])
        self.registration_page.wait_for_autofill_loader()
        if self.registration_page.get_street_value() == "":
            self.registration_page.enter_street(self.registration_data["street"])
        if self.registration_page.get_city_value() == "":
            self.registration_page.enter_city(self.registration_data["city"])
        if self.registration_page.get_state_value() == "":
            self.registration_page.enter_state(self.registration_data["state"])
        self.registration_page.click_register_button()
        error_message = self.registration_page.get_missing_email_error_message()
        self.assertIn("Email is required", error_message)