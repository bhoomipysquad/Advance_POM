from pages.open_cart_page import Open_Cart_Page


def test_open_cart_page(setup):
    driver = setup
    oc = Open_Cart_Page(driver)
    oc.open_cart_page()
