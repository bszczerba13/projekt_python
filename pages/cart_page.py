from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Locators:
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='product-title']")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, "[data-test='cart-total']")
    REMOVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a.btn-danger")
    EMPTY_CART_INFO = (By.CSS_SELECTOR, "p.ng-star-inserted")

class CartPage(BasePage):

    def get_cart_product_name(self):
            cart_product_name = self.driver.find_element(*Locators.CART_PRODUCT_NAME).text.strip()
            return cart_product_name

    def get_cart_total_price(self):
            cart_total_price = self.driver.find_element(*Locators.CART_TOTAL_PRICE).text
            return float(cart_total_price.replace('$', '').strip())

    def remove_product(self):
            self.driver.find_element(*Locators.CART_PRODUCT_NAME).click()

    def _verify_page(self):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CART_PRODUCT_NAME))
