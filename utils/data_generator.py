from faker import Faker

class RegistrationDataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.FIRST_NAME = self.fake.first_name()
        self.LAST_NAME = self.fake.last_name()
        self.DATE_OF_BIRTH = self.fake.date_of_birth(minimum_age=18).strftime("%Y-%m-%d")
        self.POSTAL_CODE = self.fake.zipcode()
        self.HOUSE_NUMBER = self.fake.pyint(min_value=1, max_value=99)
        self.PHONE_NUMBER = self.fake.random_number(digits=9)
        self.EMAIL_ADDRESS = self.fake.email()
        self.PASSWORD = self.fake.password(length=10, special_chars=True, digits=True, lower_case=True, upper_case=True)

class OrderDataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.FIRST_NAME = self.fake.first_name()
        self.LAST_NAME = self.fake.last_name()
        self.EMAIL = self.fake.email()
        self.POSTAL_CODE = self.fake.zipcode()
        self.HOUSE_NUMBER = self.fake.pyint(min_value=1, max_value=99)
        self.CREDIT_CARD_NUMBER = self.fake.numerify("####-####-####-####")
        self.CARD_EXPIRATION_DATE = self.fake.credit_card_expire(start='now', date_format="%m/%Y")
        self.CARD_CVV = self.fake.credit_card_security_code()