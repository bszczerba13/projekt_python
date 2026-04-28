from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage

class Locators:
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='product-title']")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, "[data-test='cart-total']")
    REMOVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a.btn-danger")
    EMPTY_CART_INFO = (By.CSS_SELECTOR, "p.ng-star-inserted")
    PROCEED_TO_CHECKOUT_BUTTON_CART_STEP = (By.CSS_SELECTOR, "[data-test='proceed-1']")

class CartPage(BasePage):
    """
    Page object for shopping cart page.
    """

    def get_cart_product_name(self):
        """
        Return product name from cart.
        """
        cart_product_name = self.driver.find_element(*Locators.CART_PRODUCT_NAME).text.strip()
        return cart_product_name

    def get_cart_total_price(self):
        """
        Return total cart price.
        """
        cart_total_price = self.driver.find_element(*Locators.CART_TOTAL_PRICE).text
        return float(cart_total_price.replace('$', '').strip())

    def remove_product(self):
        """
        Remove product from cart.
        """
        self.driver.find_element(*Locators.REMOVE_PRODUCT_BUTTON).click()

    def get_empty_cart_info(self):
        """
        Return empty cart message.
        """
        info = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.EMPTY_CART_INFO)).text
        return info

    def go_to_checkout(self):
        """
        Proceed to checkout.
        """
        self.driver.find_element(*Locators.PROCEED_TO_CHECKOUT_BUTTON_CART_STEP).click()
        return CheckoutPage(self.driver)

    def _verify_page(self):
        """
        Verify cart page is loaded.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CART_PRODUCT_NAME))