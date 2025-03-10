import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def enter_username(self, username):
        self.send_keys(By.ID, "user-name" , username)
        # self.send_keys(self.username_field[0], self.username_field[1], username)


    def enter_password(self, password):
        self.send_keys(By.ID, "password" , password)
        # self.send_keys(self.password_field[0], self.password_field[1], password)


    def click_login(self):
        self.click(By.ID, "login-button")
        # self.click(self.login_button[0], self.login_button[1])



    def login(self, username, password):
        """Log in using provided username and password."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(2)
        if self.driver.current_url != "https://www.saucedemo.com/":
            pass
        else:
            self.capture_screenshot("failed username.png")


