class TestCheckout:
    """
    Checkout test cases.
    """

    def test_checkout(self, product_page, order_data):
        """
        Verify guest checkout flow.
        """
        product_page.add_product_to_cart()
        cart_page = product_page.go_to_cart()
        checkout_page = cart_page.go_to_checkout()
        checkout_page.go_to_guest_tab()
        checkout_page.enter_guest_email(order_data["email_address"])
        checkout_page.enter_guest_first_name(order_data["first_name"])
        checkout_page.enter_guest_last_name(order_data["last_name"])
        checkout_page.click_continue_as_guest_button()
        guest_data = checkout_page.get_guest_data_summary()
        assert order_data["email_address"] in guest_data
        assert order_data["first_name"] in guest_data
        assert order_data["last_name"] in guest_data
        checkout_page.go_to_billing_address_step()
        checkout_page.select_guest_country()
        checkout_page.enter_postal_code(order_data["postal_code"])
        checkout_page.enter_house_number(order_data["house_number"])
        checkout_page.wait_for_autofill()
        if checkout_page.get_order_street() == "":
            checkout_page.enter_order_street(order_data["street"])
        if checkout_page.get_order_city() == "":
            checkout_page.enter_order_city(order_data["city"])
        if checkout_page.get_order_state() == "":
            checkout_page.enter_order_state(order_data["state"])
        checkout_page.go_to_payment_step()
        checkout_page.choose_payment_method("credit-card")
        checkout_page.enter_card_number(order_data["credit_card_number"])
        checkout_page.enter_card_expiration_date(order_data["card_expiration_date"])
        checkout_page.enter_card_cvv(order_data["card_cvv"])
        checkout_page.enter_card_holder_name(f"{order_data['first_name']} {order_data['last_name']}")
        checkout_page.click_confirm_button()
        payment_success_message = checkout_page.get_payment_success_message().lower()
        assert "success" in payment_success_message
        checkout_page.click_confirm_button()
        order_confirmation_message = checkout_page.get_order_confirmation_message().lower()
        assert "your invoice number" in order_confirmation_message