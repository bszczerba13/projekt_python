from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.ADD_TO_CART_BUTTON))
        button.click()

    def get_cart_quantity(self):
        """
        Return cart quantity.
        """
        quantity = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CART_QUANTITY))
        return int(quantity.text)

    def go_to_cart(self):
        """
        Open shopping cart page.
        """
        cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.CART_BUTTON))
        cart_button.click()
        return CartPage(self.driver)

    def get_product_price(self):
        """
        Return current product price.
        """
        price = self.driver.find_element(*Locators.PRODUCT_PRICE).text
        return float(price)

    def get_product_name(self):
        """
        Return current product name.
        """
        product_name = self.driver.find_element(*Locators.PRODUCT_NAME).text.strip()
        return product_name

    def _verify_page(self):
        """
        Verify product page is loaded.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.ADD_TO_CART_BUTTON))