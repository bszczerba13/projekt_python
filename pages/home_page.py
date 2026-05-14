from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

class Locators:
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='nav-sign-in']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='product-price']")
    SORT_LIST = (By.CSS_SELECTOR, "[data-test='sort']")
    SORTING_COMPLETED = (By.CSS_SELECTOR, "[data-test='sorting_completed']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-name']")
    FILTERING_COMPLETED = (By.CSS_SELECTOR, "[data-test='filter_completed']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "a[data-test^='product-']")
    OUT_OF_STOCK_PRODUCT = (By.CSS_SELECTOR, "[data-test='out-of-stock']")

class HomePage(BasePage):
    """
    Page object for the home page.
    """

    def click_sign_in(self):
        """
        Open Login page.
        """
        self.click(Locators.SIGN_IN_LINK)
        return LoginPage(self.driver)

    def get_product_prices(self):
        """
        Return list of product prices.
        """
        elements = self.get_elements(Locators.PRODUCT_PRICE)
        prices = []
        for element in elements:
            price_value = element.text.replace('$', '').strip()
            prices.append(float(price_value))
        return prices

    def sort_by(self, option):
        """
        Sort products by selected option.
        """
        self.select_by_value(Locators.SORT_LIST, option)
        self.wait_for_presence(Locators.SORTING_COMPLETED)

    def sort_price_low_to_high(self):
        """
        Sort products by price ascending.
        """
        self.sort_by('price,asc')

    def sort_price_high_to_low(self):
        """
        Sort products by price descending.
        """
        self.sort_by('price,desc')

    def get_product_titles(self):
        """
        Return list of displayed product titles.
        """
        elements = self.get_elements(Locators.PRODUCT_TITLE)
        titles = []
        for element in elements:
            titles.append(element.text.lower())
        return titles

    def filter_by_category(self, category):
        """
        Filter products by category.
        """
        locator = (By.XPATH, f"//label[contains(text(), '{category}')]")
        self.click(locator)
        self.wait_for_presence(Locators.FILTERING_COMPLETED)

    def open_first_available_product(self):
        """
        Open first available product page.
        """
        products = self.get_elements(Locators.PRODUCT_CARDS)
        for product in products:
            out_of_stock = product.find_elements(*Locators.OUT_OF_STOCK_PRODUCT)
            if not out_of_stock:
                product.click()
                return ProductPage(self.driver)
        raise Exception("No available products found")

    def _verify_page(self):
        """
        Verify home page is loaded.
        """
        self.wait_for_visibility(Locators.SORT_LIST)
        self.wait_for_visibility(Locators.PRODUCT_CARDS)