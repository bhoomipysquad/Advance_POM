import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Social_Media(BasePage):
    def open_social_media_pages(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        social_media_pages = { "twitter" : "//a[normalize-space()='Twitter']" ,
                               "facebook" : "//a[normalize-space()='Facebook']" ,
                               "linkedin" : "//a[normalize-space()='LinkedIn']"
                              }
        for page,xpath in social_media_pages.items():
            self.click(By.XPATH , xpath)
            self.windows_and_scroll()
