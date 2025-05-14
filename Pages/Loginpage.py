from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage
import time
class LoginPage(BasePage):
    username_input = (By.XPATH, "//input[@name='username']")
    password_input = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[@type='submit']")
    name_message= (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
    pass_message= (By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
    invalid_message=(By.XPATH,"//div[@class='oxd-alert-content oxd-alert-content--error']")
    def login(self, uname, pwd):
        self.send_keys(self.username_input, uname)
        self.send_keys(self.password_input, pwd)
        self.click(self.login_button)
        time.sleep(5)
        
    def get_name_msg(self):
        return self.get_text(self.name_message)
    def get_pass_msg(self):
        return self.get_text(self.pass_message)
    def get_invalid_msg(self):
        return self.get_text(self.invalid_message)
    




