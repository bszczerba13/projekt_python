import allure
from selenium.webdriver.common.by import By
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
        return self.get_text(Locators.CART_PRODUCT_NAME).strip()

    def get_cart_total_price(self):
        """
        Return total cart price.
        """
        return float(self.get_text(Locators.CART_TOTAL_PRICE).replace('$', '').strip())

    @allure.step("Remove product")
    def remove_product(self):
        """
        Remove product from cart.
        """
        self.click(Locators.REMOVE_PRODUCT_BUTTON)

    def get_empty_cart_info(self):
        """
        Return empty cart message.
        """
        return self.get_text(Locators.EMPTY_CART_INFO)

    @allure.step("Proceed to checkout")
    def go_to_checkout(self):
        """
        Proceed to checkout.
        """
        self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON_CART_STEP)
        return CheckoutPage(self.driver)

    def _verify_page(self):
        """
        Verify cart page is loaded.
        """
        self.wait_for_visibility(Locators.CART_PRODUCT_NAME)