from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage

class Locators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart']")
    CART_BUTTON = (By.CSS_SELECTOR, "[data-test='nav-cart']")
    CART_QUANTITY = (By.CSS_SELECTOR, "[data-test='cart-quantity']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='unit-price']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='product-name']")

class ProductPage(BasePage):
    """
    Page object for product details page.
    """
    def add_product_to_cart(self):
        """
        Add product to cart.
        """
        self.click(Locators.ADD_TO_CART_BUTTON)

    def get_cart_quantity(self):
        """
        Return cart quantity.
        """
        return int(self.get_text(Locators.CART_QUANTITY))

    def go_to_cart(self):
        """
        Open shopping cart page.
        """
        self.click(Locators.CART_BUTTON)
        return CartPage(self.driver)

    def get_product_price(self):
        """
        Return current product price.
        """
        return float(self.get_text(Locators.PRODUCT_PRICE))

    def get_product_name(self):
        """
        Return current product name.
        """
        return self.get_text(Locators.PRODUCT_NAME)

    def _verify_page(self):
        """
        Verify product page is loaded.
        """
        self.wait_for_visibility(Locators.ADD_TO_CART_BUTTON)