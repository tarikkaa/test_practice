import time

from utilities import xlUtil
from utilities.BaseClass import BaseClass
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage

class TestDataDrivenLogin(BaseClass):

    def test_data_driven_login(self):
        loginPage = LoginPage(self.driver)
        mainPage = MainPage(self.driver)
        path = "C:\\Users\\taras.andrushchak\\PycharmProjects\\test_practice\\utilities\\Login.xlsx"
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
                print("test is passed")
                xlUtil.writeData(path, 'Sheet1', row, 3, "test passed")
                self.waitElement(mainPage.account_button)
                mainPage.gotoAccountSection()
                self.waitElement(mainPage.logout_button)
                mainPage.logOut()
            else:
                print("wrong credentials - test passed")
                xlUtil.writeData(path, 'Sheet1', row, 3, 'test failed')
                assert self.driver.title != "(1) Facebook"













