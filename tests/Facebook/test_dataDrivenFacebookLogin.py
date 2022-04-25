import time

import pytest
import pytest_check as check
from pytest_check import check_func

from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from utilities import xlUtil
from utilities.BaseClass import BaseClass

@pytest.mark.datadriven
class TestDataDrivenLogin(BaseClass):

    @check_func
    def is_main_page_title(self, a):
        assert a == "(1) Facebook"


    def test_data_driven_login(self):
        loginPage = LoginPage(self.driver)
        mainPage = MainPage(self.driver)
        path = "/utilities/test_data/Login.xlsx"
        rows = xlUtil.getRowCount(path, 'Sheet1')
        for row in range(2, rows+1):
            login = xlUtil.readData(path, 'Sheet1', row, 1)
            password = xlUtil.readData(path, 'Sheet1', row, 2)
            loginPage.load()
            self.waitElement(loginPage.login_field)
            loginPage.getLoginField().send_keys(login)
            loginPage.getPasswordField().send_keys(password)
            loginPage.clickLoginButton()
            time.sleep(3)
            if self.driver.title == "(1) Facebook":
                pytest.skip("not need to test negative cases")
                xlUtil.writeData(path, 'Sheet1', row, 3, "test passed")
                check.equal(self.driver.title, "(1) Facebook")
                mainPage.gotoAccountSection()
                self.waitElement(MainPage.logout_button)
                mainPage.logOut()
            else:
                xlUtil.writeData(path, 'Sheet1', row, 3, 'test failed')
                #check.equal (self.driver.title, "(1) Facebook")
                title = self.driver.title
                self.is_main_page_title(title)














