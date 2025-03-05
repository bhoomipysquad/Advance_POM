from pages.add_to_cart import Add_To_Cart


def test_add_to_cart(setup):
    driver = setup
    atk = Add_To_Cart(driver)
    atk.add_to_cart_item()
    atk.to_add_specific_item()
