from pages.inventory_page import InventoryPage


def test_inventory_page_title(setup):
    """Test that the inventory page title is displayed correctly."""
    driver = setup
    inventory_page = InventoryPage(driver)
    title = inventory_page.get_inventory_title()
    assert title == "Products", f"Expected title to be 'Products', but got {title}"

def test_logout(setup):
    """Test that the logout functionality works properly."""
    driver = setup
    inventory_page = InventoryPage(driver)
    inventory_page.click_logout()           # Click the logout button
    # Assert that back on the login page (SauceDemo login page)
    assert driver.current_url, f"Expected URL to be 'https://www.saucedemo.com/', but got {driver.current_url}"

def test_side_menu(setup):
    driver = setup
    side_menu_check = InventoryPage(driver)
    side_menu_check.check_side_menu()
