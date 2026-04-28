from faker import Faker

class DataGenerator:
    """
    Generate test data for automated tests.
    """
    def __init__(self):
        self.fake = Faker()

    def registration_data_generator(self):
        """
        Generate registration test data.
        """
        return {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "date_of_birth": self.fake.date_of_birth(minimum_age=18, maximum_age=70).strftime("%Y-%m-%d"),
            "postal_code": self.fake.zipcode(),
            "house_number": self.fake.pyint(min_value=1, max_value=99),
            "phone_number": self.fake.random_number(digits=9),
            "email_address": self.fake.email(),
            "password": self.fake.password(length=10, special_chars=True, digits=True, lower_case=True, upper_case=True),
            "street": self.fake.street_name(),
            "city": self.fake.city(),
            "state": self.fake.state(),
        }

    def order_data_generator(self):
        """
        Generate checkout order test data.
        """
        return {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "email_address": self.fake.email(),
            "postal_code": self.fake.zipcode(),
            "house_number": self.fake.pyint(min_value=1, max_value=99),
            "credit_card_number": self.fake.numerify("####-####-####-####"),
            "card_expiration_date": self.fake.credit_card_expire(start='now', date_format="%m/%Y"),
            "card_cvv": self.fake.credit_card_security_code(),
            "street": self.fake.street_name(),
            "city": self.fake.city(),
            "state": self.fake.state(),
        }

    def invalid_login_data_generator(self):
        """
        Generate invalid login credentials.
        """
        return {
            "email_address": self.fake.email(),
            "password": self.fake.password(length=5),
        }