class TestCart:
    """
    Shopping cart test cases.
    """

    def test_add_product_to_cart(self, product_page):
        """
        Verify adding product to cart.
        """
        product_page.add_product_to_cart()
        quantity = product_page.get_cart_quantity()
        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()
        assert quantity == 1
        cart_page = product_page.go_to_cart()
        cart_product_name = cart_page.get_cart_product_name()
        cart_total_price = cart_page.get_cart_total_price()
        assert product_name == cart_product_name
        assert product_price * quantity == cart_total_price

    def test_remove_product_from_cart(self, product_page):
        """
        Verify removing product from cart.
        """
        product_page.add_product_to_cart()
        cart_page = product_page.go_to_cart()
        cart_page.remove_product()
        empty_cart_info = cart_page.get_empty_cart_info()
        assert "The cart is empty" in empty_cart_info