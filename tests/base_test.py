import unittest
from selenium import webdriver
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    """
    Base test class for all test cases.
    """
    def setUp(self):
        """
        Set up browser and open home page.
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://practicesoftwaretesting.com/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """
        Close browser after test.
        """
        self.driver.quit()