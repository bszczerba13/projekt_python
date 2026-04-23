from tests.base_test import BaseTest


class TestCart(BaseTest):
    def setUp(self):
        super().setUp()
        self.product_page = self.home_page.open_first_available_product()

    def test_add_product_to_cart(self):
        self.product_page.add_product_to_cart()
        quantity = self.product_page.get_cart_quantity()
        self.assertEqual(1, quantity)