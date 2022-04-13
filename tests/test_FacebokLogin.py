import pytest

from pageObjects.FacebookLoginPage import FacebookLoginPage
from utilities.BaseClass import BaseClass
from utilities.TestData import TestData


class FacebookTest(BaseClass):

    def test_login(self):
        self.getNewLink("https://uk-ua.facebook.com/")
        loginPage = FacebookLoginPage(self.driver)
        loginPage.enterLogin()
        loginPage.enterPassword()
        loginPage.clickLoginButton()
        username = loginPage.getMainPageUser()
        assert username == TestData.userName

























