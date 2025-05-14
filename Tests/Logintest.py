import pytest
import time
from Pages.Loginpage import LoginPage
from Utils.excelReader import get_data
from selenium.webdriver.common.by import By

test_data = get_data("C:\Python_Selenium\POM_OrangeHrm\Excel\LoginORM.xlsx", "Sheet1")
@pytest.mark.usefixtures("setup_and_teardown")
class TestLoginFromExcel:

    @pytest.mark.parametrize("username, password",test_data)
    def test_login_excel(self, username, password):
        login_page = LoginPage(self.driver)

        login_page.login(username, password)

        if username==" ":
            time.sleep(5)
            error_msg = login_page.get_name_msg()
            assert "Required" in error_msg
        elif password==" ":
            time.sleep(5)
            error_msg = login_page.get_pass_msg()
            assert "Required" in error_msg
      
        elif username != "Admin" or password != "admin123":
            time.sleep(5)
            error_msg = login_page.get_invalid_msg()
            assert "Invalid credentials" in error_msg

        elif username == "Admin" and password == "admin123":
            exp="Dashboard"
            act=self.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
            assert exp==act
            exp1="Leave"
            act1=self.driver.find_element(By.XPATH,"(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[3]").text
            assert exp1==act1
            exp2="Time"
            act2=self.driver.find_element(By.XPATH,"(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[4]").text
            assert exp2==act2
        
