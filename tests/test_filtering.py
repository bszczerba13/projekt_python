from tests.base_test import BaseTest

class TestFiltering(BaseTest):
    """
    Product filtering test cases.
    """
    def setUp(self):
        """
         Set up for filtering test.
        """
        super().setUp()

    def test_filter_hammer(self):
        """
        Verify filtering products by Hammer category.
        """
        category = "Hammer"
        self.home_page.filter_by_category(category)
        product_titles = self.home_page.get_product_titles()
        for product_title in product_titles:
            self.assertIn(category.lower(), product_title)