# to test that url successfully work with given username and password

def test_conf_test1(setup):
    driver = setup

    act_url = driver.current_url
    if act_url == "https://www.saucedemo.com/inventory.html":
        assert True
        driver.close()
    else:
        driver.save_screenshot("openurl.png")
        assert False


#to test that Url successfully opened
def test_conf_test2(setup1):
    driver = setup1

    assert driver.current_url == "https://www.saucedemo.com/"