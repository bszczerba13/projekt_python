from pages.login_page import LoginPage

class TestRegistration:
    """
    Registration test cases.
    """
    def test_registration(self, registration_page, registration_data, driver):
        """
        Verify successful user registration.
        """
        registration_page.enter_first_name(registration_data["first_name"])
        registration_page.enter_last_name(registration_data["last_name"])
        registration_page.enter_date_of_birth(registration_data["date_of_birth"])
        registration_page.select_country()
        registration_page.enter_postal_code(registration_data["postal_code"])
        registration_page.enter_house_number(registration_data["house_number"])
        registration_page.wait_for_autofill_loader()
        registration_page.enter_phone(registration_data["phone_number"])
        registration_page.enter_registration_email(registration_data["email_address"])
        registration_page.enter_registration_password(registration_data["password"])
        if registration_page.get_street_value() == "":
            registration_page.enter_street(registration_data["street"])
        if registration_page.get_city_value() == "":
            registration_page.enter_city(registration_data["city"])
        if registration_page.get_state_value() == "":
            registration_page.enter_state(registration_data["state"])
        registration_page.click_register_button()
        login_page = LoginPage(driver)
        assert login_page.is_page_title_visible()

    def test_registration_missing_email(self, registration_page, registration_data):
        """
        Verify registration validation when email is missing.
        """
        registration_page.enter_first_name(registration_data["first_name"])
        registration_page.enter_last_name(registration_data["last_name"])
        registration_page.enter_date_of_birth(registration_data["date_of_birth"])
        registration_page.select_country()
        registration_page.enter_postal_code(registration_data["postal_code"])
        registration_page.enter_house_number(registration_data["house_number"])
        registration_page.wait_for_autofill_loader()
        registration_page.enter_phone(registration_data["phone_number"])
        registration_page.enter_registration_password(registration_data["password"])
        if registration_page.get_street_value() == "":
            registration_page.enter_street(registration_data["street"])
        if registration_page.get_city_value() == "":
            registration_page.enter_city(registration_data["city"])
        if registration_page.get_state_value() == "":
            registration_page.enter_state(registration_data["state"])
        registration_page.click_register_button()
        error_message = registration_page.get_missing_email_error_message()
        assert "Email is required" in error_message