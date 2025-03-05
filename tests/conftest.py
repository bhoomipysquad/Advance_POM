import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def setup():
    """Setup WebDriver and login."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")  # SauceDemo login page
    # Login to the application with a valid user
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")  # Log in with a valid user
    yield driver
    driver.quit()


@pytest.fixture
def setup1():
    # Setup WebDriver (browser)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")  # SauceDemo login page
    yield driver
    driver.quit()