import pytest
from pages.account_page import AccountPage
import utils.csv_reader

class TestLogin:
    """
    Login test cases.
    """
    @pytest.mark.parametrize("email,password,role", utils.csv_reader.get_csv_data("test_data/users.csv"))

    def test_login(self, login_page,driver, email, password, role):
        """
        Verify login for different user roles.
        """
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()
        if login_page.is_account_locked():
            pytest.skip("User account locked")
        account_page = AccountPage(driver)
        page_title = account_page.get_page_title()
        if role == "admin":
            assert "Sales over the years" in page_title
        elif role == "user":
            assert "My account" in page_title
        else:
            pytest.fail(f"Unexpected role: {role}")

    def test_invalid_login_data(self, login_page, invalid_login_data):
        """
        Verify login fails with invalid credentials.
        """
        login_page.enter_email(invalid_login_data["email_address"])
        login_page.enter_password(invalid_login_data["password"])
        login_page.click_login_button()
        error_message = login_page.get_invalid_login_error()
        assert "Invalid email or password" in error_message