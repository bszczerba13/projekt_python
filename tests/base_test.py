import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://practicesoftwaretesting.com/")

    def tearDown(self):
        self.driver.quit()