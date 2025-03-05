from selenium.webdriver.common.by import By
from .base_page import BasePage

class Open_Cart_Page(BasePage):
    # cart page elements
    cart_button = (By.CLASS_NAME,"shopping_cart_link")
    check_out_button = (By.XPATH , "//button[@id='checkout']")
    first_name = (By.XPATH , "//input[@id='first-name']")
    last_name = (By.XPATH , "//input[@id='last-name']")
    postal_code = (By.XPATH , "//input[@id='postal-code']")
    continue_button = (By.XPATH , "//input[@id='continue']")
    finish_button = (By.XPATH , "//button[@id='finish']")
    back_home_button = (By.XPATH , "//button[@id='back-to-products']")

    def open_cart_page(self):
        self.click(By.CLASS_NAME , "shopping_cart_link")
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html"
        self.click(By.XPATH , "//button[@id='checkout']")   # to click on checkout button
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
        self.send_keys(By.XPATH , "//input[@id='first-name']" , "ABCD")
        self.send_keys(By.XPATH , "//input[@id='last-name']" , "Patel" )
        self.send_keys(By.XPATH , "//input[@id='postal-code']" , "98785" )
        self.click(By.XPATH , "//input[@id='continue']")
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
        self.click(By.XPATH , "//button[@id='finish']")
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
        self.click(By.XPATH , "//button[@id='back-to-products']")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

