from tests.base_test import BaseTest


class SortingTest(BaseTest):
    """
    Product sorting test cases.
    """
    def setUp(self):
        """
        Set up for sorting tests.
        """
        super().setUp()

    def test_sort_price_low_to_high(self):
        """
        Verify sorting by price ascending.
        """
        self.home_page.sort_price_low_to_high()
        prices = self.home_page.get_product_prices()
        self.assertEqual(sorted(prices), prices)

    def test_sort_price_high_to_low(self):
        """
        Verify sorting by price descending.
        """
        self.home_page.sort_price_high_to_low()
        prices = self.home_page.get_product_prices()
        self.assertEqual(sorted(prices, reverse=True), prices)