class TestSorting:
    """
    Product sorting test cases.
    """
    def test_sort_price_low_to_high(self, home_page):
        """
        Verify sorting by price ascending.
        """
        home_page.sort_price_low_to_high()
        prices = home_page.get_product_prices()
        assert prices == sorted(prices)

    def test_sort_price_high_to_low(self, home_page):
        """
        Verify sorting by price descending.
        """
        home_page.sort_price_high_to_low()
        prices = home_page.get_product_prices()
        assert prices == sorted(prices, reverse=True)