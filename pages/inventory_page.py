import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    # Inventory page elements
    inventory_title = (By.CLASS_NAME, "title")
    side_menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.XPATH , "//a[@id='logout_sidebar_link']")
    close_button = (By.XPATH , "//button[@id='react-burger-cross-btn']")


    def get_inventory_title(self):
        """Check if  the inventory page by verifying the title."""
        self.wait_for_element(self.inventory_title[0], self.inventory_title[1])
        return self.driver.find_element(self.inventory_title[0], self.inventory_title[1]).text


    def check_side_menu(self):
        self.click(By.ID, "react-burger-menu-btn")  # click on side menu
        time.sleep(2)
        self.click(By.XPATH , "//button[@id='react-burger-cross-btn']")
        time.sleep(1)
        side_menu_options = {
                    "About": "//a[@id='about_sidebar_link']",
                    "Logout": "//a[@id='logout_sidebar_link']"
                    }
        for side_menu ,xpath in side_menu_options.items():
            self.click(By.ID , "react-burger-menu-btn") #click on side menu
            self.click(By.XPATH, xpath)  # click on specific side menu
            self.hover_and_check_images()
            self.driver.back()


    def click_logout(self):
        """Click the logout button."""
        self.click(self.side_menu_button[0], self.side_menu_button[1])
        self.click(self.logout_button[0], self.logout_button[1])
