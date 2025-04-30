import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"), ("locked_out_user", "secret_sauce"),
                                               ("problem_user", "secret_sauce") , ("performance_glitch_user", "secret_sauce") ,
                                               ("error_user", "secret_sauce")   , ("visual_user", "secret_sauce")])

def test_login_with_valid_invalid_inputs(setup1,username,password):
    driver = setup1
    login_page = LoginPage(driver)
    login_page.login(username,password)
    # assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    print("current url is ---->   " , driver.current_url)
    assert  driver.current_url.endswith("/inventory.html")