from selenium.webdriver.common.by import By
from .base_page import BasePage


class Add_To_Cart(BasePage):
    # add to cart page elements
    add_to_cart = (By.XPATH , "//button[@id='add-to-cart-sauce-labs-backpack']")
    cart_button = (By.CLASS_NAME,"shopping_cart_link")
    continue_shopping = (By.XPATH , "//button[@id='continue-shopping']")
    remove = (By.XPATH , "//button[@id='remove-sauce-labs-backpack']")
    specific_item = (By.LINK_TEXT , "Test.allTheThings() T-Shirt (Red)")
    add_specific_item = (By.XPATH , "//button[@id='add-to-cart']")
    back_to_products = (By.XPATH , "//button[@id='back-to-products']")

    def add_to_cart_item(self):
        # self.scroll_up_down()
        # self.click(By.XPATH , "//button[@id='add-to-cart-sauce-labs-backpack']")
        # self.click(By.CLASS_NAME,"shopping_cart_link")
        # self.click(By.XPATH , "//button[@id='continue-shopping']")
        # self.click(By.XPATH , "//button[@id='remove-sauce-labs-backpack']")

        # def add_backpack_to_cart(self):
            self.scroll_up_down()
            for locator in [self.add_to_cart, self.cart_button, self.continue_shopping, self.remove]:
                self.click(*locator)


    def to_add_specific_item(self):
        # self.click(By.LINK_TEXT , "Test.allTheThings() T-Shirt (Red)")
        # self.click(By.XPATH , "//button[@id='add-to-cart']")
        # self.click(By.XPATH , "//button[@id='back-to-products']")

          # def add_specific_item(self):
                 for locator in [self.specific_item, self.add_specific_item, self.back_to_products]:
                     self.click(*locator)