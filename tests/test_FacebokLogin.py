import pytest

from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from utilities.BaseClass import BaseClass
from utilities.TestData import TestData


class FacebookTest(BaseClass):

    def test_login_page_title(self):
        loginPage = LoginPage(self.driver)
        loginPage.load()
        assert loginPage.getPageTitle() == TestData.loginPageTitle

    def test_login_success(self):
        loginPage = LoginPage(self.driver)
        mainPage = MainPage(self.driver)

        loginPage.load()
        loginPage.enterLogin()
        loginPage.enterPassword()
        loginPage.clickLoginButton()
        assert mainPage.getUsername() == TestData.userName

































