from tests.base_test import BaseTest


class TestCart(BaseTest):
    def setUp(self):
        super().setUp()
        self.product_page = self.home_page.open_first_available_product()

    def test_add_product_to_cart(self):
        self.product_page.add_product_to_cart()
        quantity = self.product_page.get_cart_quantity()
        product_name = self.product_page.get_product_name()
        product_price = self.product_page.get_product_price()
        self.assertEqual(1, quantity)
        self.cart_page = self.product_page.go_to_cart()
        cart_product_name = self.cart_page.get_cart_product_name()
        cart_total_price = self.cart_page.get_cart_total_price()
        self.assertEqual(product_name, cart_product_name)
        self.assertEqual(product_price*quantity, cart_total_price)

    def test_remove_product_from_cart(self):
        self.product_page.add_product_to_cart()
        self.cart_page = self.product_page.go_to_cart()
        self.cart_page.remove_product()
        empty_cart_info = self.cart_page.get_empty_cart_info()
        self.assertIn("The cart is empty", empty_cart_info)