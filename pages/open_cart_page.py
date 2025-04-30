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
        self.send_keys(By.XPATH , "//input[@id='first-name']" , "Riya")
        self.send_keys(By.XPATH , "//input[@id='last-name']" , "Patel" )
        self.send_keys(By.XPATH , "//input[@id='postal-code']" , "98785" )
        self.click(By.XPATH , "//input[@id='continue']")
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
        self.click(By.XPATH , "//button[@id='finish']")
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
        self.click(By.XPATH , "//button[@id='back-to-products']")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    # def open_cart_page(self):
    #     self.click(*self.cart_button)
    #     assert self.driver.current_url.endswith("/cart.html")
    #
    #     self.click(*self.check_out_button)
    #     assert self.driver.current_url.endswith("/checkout-step-one.html")
    #
    #     form_data = {
    #                     self.first_name: "Riya",
    #                     self.last_name: "Patel",
    #                     self.postal_code: "98785"
    #                  }
    #
    #     for locator, value in form_data.items():
    #         self.send_keys(*locator, value)
    #
    #     self.click(*self.continue_button)
    #     assert self.driver.current_url.endswith("/checkout-step-two.html")
    #
    #     self.click(*self.finish_button)
    #     assert self.driver.current_url.endswith("/checkout-complete.html")
    #
    #     self.click(*self.back_home_button)
    #     assert self.driver.current_url.endswith("/inventory.html")
