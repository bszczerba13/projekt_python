import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

class Locators:
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='nav-sign-in']")
    CART_BUTTON = (By.CSS_SELECTOR, "[data-test='nav-cart']")
    CART_QUANTITY = (By.CSS_SELECTOR, "[data-test='cart-quantity']")

class HeaderComponent(BasePage):
    """
    Header component actions.
    """

    @allure.step("Open login page")
    def click_sign_in(self):
        """
        Open Login page.
        """
        self.click(Locators.SIGN_IN_LINK)
        return LoginPage(self.driver)

    def get_cart_quantity(self):
        """
        Return cart quantity.
        """
        return int(self.get_text(Locators.CART_QUANTITY))

    @allure.step("Open shopping cart")
    def go_to_cart(self):
        """
        Open shopping cart page.
        """
        self.click(Locators.CART_BUTTON)
        return CartPage(self.driver)