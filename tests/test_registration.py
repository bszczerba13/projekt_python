from utils.data_generator import RegistrationDataGenerator
from tests.base_test import BaseTest

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = self.home_page.click_sign_in()
        self.registration_page = self.login_page.click_register_link()
        self.data = RegistrationDataGenerator()

    def test_registration(self):
        self.registration_page.enter_first_name(self.data.FIRST_NAME)
        self.registration_page.enter_last_name(self.data.LAST_NAME)
        self.registration_page.enter_date_of_birth(self.data.DATE_OF_BIRTH)
        self.registration_page.select_country()
        self.registration_page.enter_postal_code(self.data.POSTAL_CODE)
        self.registration_page.enter_house_number(self.data.HOUSE_NUMBER)
        self.registration_page.enter_phone(self.data.PHONE_NUMBER)
        self.registration_page.enter_registration_email(self.data.EMAIL_ADDRESS)
        self.registration_page.enter_registration_password(self.data.PASSWORD)
        self.registration_page.click_register_button()
        self.assertTrue(self.login_page.is_page_title_visible())