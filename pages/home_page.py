from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='nav-sign-in']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='product-price']")
    SORT_LIST = (By.CSS_SELECTOR, "[data-test='sort']")
    SORTING_COMPLETED = (By.CSS_SELECTOR, "[data-test='sorting_completed']")

class HomePage(BasePage):
    """
    Home Page Object
    """

    def click_sign_in(self):
        self.driver.find_element(*Locators.SIGN_IN_LINK).click()
        return LoginPage(self.driver)

    def get_product_prices(self):
        elements = self.driver.find_elements(*Locators.PRODUCT_PRICE)
        prices = []
        for element in elements:
            price_value = element.text.replace('$', '').strip()
            prices.append(float(price_value))
        return prices

    def sort_by(self, option):
        sort_options = self.driver.find_element(*Locators.SORT_LIST)
        select = Select(sort_options)
        select.select_by_value(option)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.SORTING_COMPLETED))

    def sort_price_low_to_high(self):
        self.sort_by('price,asc')

    def sort_price_high_to_low(self):
        self.sort_by('price,desc')

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.SORT_LIST))