from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class Locators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart']")
    CART_BUTTON = (By.CSS_SELECTOR, "[data-test='nav-cart']")
    CART_QUANTITY = (By.CSS_SELECTOR, "[data-test='cart-quantity']")

class ProductPage(BasePage):

    def add_product_to_cart(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.ADD_TO_CART_BUTTON))
        button.click()

    def get_cart_quantity(self):
        quantity = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CART_QUANTITY))
        return int(quantity.text)

    def go_to_cart(self):
        cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.CART_BUTTON))
        cart_button.click()

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.ADD_TO_CART_BUTTON))