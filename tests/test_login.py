from ddt import ddt, data, unpack
from selenium.webdriver import Keys
from utils.data_generator import DataGenerator
import utils.csv_reader
from tests.base_test import BaseTest

@ddt
class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = self.home_page.click_sign_in()

    @data(*utils.csv_reader.get_csv_data("test_data/users.csv"))
    @unpack

    def test_login(self, email, password, role):
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        account_page = self.login_page.click_login_button()
        page_title = account_page.get_page_title()
        if role == "admin":
            self.assertEqual("Sales over the years", page_title)
        elif role == "user":
            self.assertEqual("My account", page_title)

    def test_invalid_login_data(self):
        self.invalid_data = DataGenerator().invalid_login_data_generator()
        self.login_page.enter_email(self.invalid_data["email_address"])
        self.login_page.enter_password(self.invalid_data["password"] + Keys.ENTER)
        error_message = self.login_page.get_invalid_login_error()
        self.assertIn("Invalid email or password", error_message)