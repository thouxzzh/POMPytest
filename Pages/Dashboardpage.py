from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Basepage import BasePage

class DashboardPage(BasePage):
    dashboard_text = (By.XPATH, "//h6[text()='Dashboard']")
    leave_sidebar = (By.XPATH, "//span[text()='Leave']")
    time_sidebar = (By.XPATH, "//span[text()='Time']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        super().__init__(driver)

    def is_dashboard_visible(self):
        return self.is_visible(self.dashboard_text)

    def is_leave_visible(self):
        return self.is_visible(self.leave_sidebar)

    def is_time_visible(self):
        return self.is_visible(self.time_sidebar)