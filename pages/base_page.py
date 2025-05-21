from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value):
        """Wait for an element to be visible."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))

    def click(self, by, value):
        """Click an element."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.click()
        time.sleep(2)

    def send_keys(self, by, value, text):
        """Send text to an input field."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.clear()  # Clear existing text
        element.send_keys(text)
        time.sleep(1)

    def get_page_title(self):
        """Get the title of the current page."""
        return self.driver.title

    def get_current_url(self):
        """Get the current URL of the page."""
        return self.driver.current_url

    def scroll_up_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        """Scroll Down by Pixels	---    window.scrollBy(0, 500);
           Scroll Up by Pixels	    ---    window.scrollBy(0, -500);
           Scroll to Bottom	        ---    window.scrollTo(0, document.body.scrollHeight);
           Scroll to Top	        ---    window.scrollTo(0, 0);
           Scroll to Element	    ---    arguments[0].scrollIntoView();   
"""

    def switch_window(self):
        original_window = self.driver.window_handles[0]
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(original_window)
        time.sleep(2)

    def windows_and_scroll(self):
        original_window = self.driver.window_handles[0]
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(original_window)
        time.sleep(2)


    def hover_and_check_images(self):
        """Scroll down and up to check images."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def double_click_element(self, by, value):
        """Double-click an element."""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        time.sleep(2)

    def enter_text(self, by, value, text):
        """Enter text into a field."""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
        element.clear()  # clear input
        element.send_keys(text)

    def get_text(self, by, value):
        """Get text from an element."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        return element.text

    def select_dropdown_by_text(self, by, value, text):
        """Select a dropdown option by visible text."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_dropdown_by_value(self, by, value, dropdown_value):
        """Select a dropdown option by value."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        select = Select(element)
        select.select_by_value(dropdown_value)

    def select_dropdown_by_index(self, by, value, index):
        """Select a dropdown option by index."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        select = Select(element)
        select.select_by_index(index)

    def clear_input(self, by, value):
        """Clear the input field."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.clear()

    def switch_to_iframe(self, by, value):
        """Switch to an iframe."""
        iframe = self.driver.find_element(by, value)
        self.driver.switch_to.frame(iframe)

    def switch_to_default_content(self):
        """Switch back to the default content."""
        self.driver.switch_to.default_content()

    def right_click(self, by, value):
        """Right-click (context click) on an element."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()
        time.sleep(2)

    def drag_and_drop(self, by_source, value_source, by_target, value_target):
        """Drag and drop from one element to another."""
        source = self.driver.find_element(by_source, value_source)
        target = self.driver.find_element(by_target, value_target)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        time.sleep(2)

    def get_element_attribute(self, by, value, attribute):
        """Get an attribute value from an element."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        return element.get_attribute(attribute)

    def switch_to_alert(self):
        """Switch to the alert and return the alert object."""
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        return alert

    def accept_alert(self):
        """Accept the alert."""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

    def dismiss_alert(self):
        """Dismiss the alert."""
        alert = self.switch_to_alert()
        alert.dismiss()

    def wait_for_element_to_be_clickable(self, by, value):
        """Wait for an element to be clickable."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value)))

    def scroll_into_view(self, by, value):
        """To scroll an element into view if it's not visible."""
        """Scroll the element into view."""
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

    def capture_screenshot(self, file_name):
        """Capture a screenshot and save it to the specified file."""
        self.driver.save_screenshot(file_name)

    def get_browser_logs(self):
        """Get the browser console logs."""
        return self.driver.get_log('browser')

    def get_window_handles(self):
        """Get all window handles."""
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        """Switch to a window based on its handle."""
        self.driver.switch_to.window(window_handle)

    def close_current_window(self):
        """Close the current browser window."""
        self.driver.close()

    def switch_to_parent_window(self):
        """Switch back to the parent window."""
        self.driver.switch_to.window(self.driver.window_handles[0])



    """
     Measuring Test Coverage
     To check which parts of your code are tested:
                                 pytest --cov=my_project --cov-report=html
     Generates an HTML report of test coverage.
     
     
     Run only marked tests:
                                 pytest -m slow



    # Run tests in 4 parallel processes
                                 pytest -n 4  
               
               
                                
    Generate HTML test reports:
                                pip install pytest-html
                                pytest --html=report.html
                                
    
    Retries flaky tests automatically.
                                pip install pytest-rerunfailures
                                pytest --reruns 3  # Retry failed tests up to 3 times
                                
                                
    Run a specific test::      pytest test_file.py::test_addition
                               
                            
                            
    Task	           Command
Run all tests	       pytest
Run one file	       pytest test_file.py
Run one test	       pytest -k test_name
Show print/logs	       pytest -s
With verbose	       pytest -v
    
    
    
    
    
    
    
    How to Install Multiple Plugins at Once?
    pip install pytest-xdist pytest-mock pytest-cov pytest-html pytest-rerunfailures pytest-django


     
    """

"""
 Daily Steps (with Simple Commands):
    
🔢	What to Do                                      	Why	                                               Command / Action
1️⃣	Get the project                     	Download project from GitHub	                git clone <url> or use File → Get from GitHub
2️⃣	Make a new branch	                    So your work doesn’t disturb main	            git checkout -b new-feature
3️⃣	Do your work	                        Write code or fix bugs	                         (code as usual)
4️⃣	Check changes	                        See what files were changed	                    git status
5️⃣	Add files to git	                    Tell Git what you changed	                    git add .
6️⃣	Save with a message                 	Like a "save point"	                            git commit -m "what you did"
7️⃣	Upload to GitHub	                    Share your work with your team              	git push -u origin new-feature
8️⃣	Open Pull Request                   	Ask to merge your work to main	                Go to GitHub → "Compare & Pull Request"
9️⃣	Get latest from team                	Keep your code updated	                        git pull origin main
🔟	Merge a branch	                        Combine another branch into yours           	git merge branch-name
🔁	Undo last save (if mistake)	            Fix a commit mistake	                        git reset --soft HEAD~1



"""




