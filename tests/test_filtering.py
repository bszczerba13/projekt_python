class TestFiltering:
    """
    Product filtering test cases.
    """

    def test_filter_hammer(self, home_page):
        """
        Verify filtering products by Hammer category.
        """
        category = "Hammer"
        home_page.filter_by_category(category)
        product_titles = home_page.get_product_titles()
        for product_title in product_titles:
            assert category.lower() in product_title