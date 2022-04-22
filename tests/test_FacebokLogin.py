import pytest

from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from utilities.BaseClass import BaseClass
from utilities.TestData import TestData


class FacebookTest(BaseClass):

    def test_login_page_title(self):
        loginPage = LoginPage(self.driver)
        loginPage.load()
        try:
            assert self.getPageTitle() == 111
        except AssertionError as error:
            print(f"First assert fails: {error}")
        assert self.getPageTitle() == TestData.loginPageTitle


    def test_login_logout(self):
        loginPage = LoginPage(self.driver)
        mainPage = MainPage(self.driver)

        loginPage.load()
        loginPage.enterLogin()
        loginPage.enterPassword()
        loginPage.clickLoginButton()
        self.waitPageTitle(TestData.mainPageTitle)
        assert self.getPageTitle() == TestData.mainPageTitle
        # assert mainPage.getUsername() == TestData.userName
        mainPage.gotoAccountSection()
        self.waitElement(mainPage.logout_button)
        mainPage.logOut()
        assert self.getPageTitle() == TestData.loginPageTitle


    def test_login_wrong_password(self):
        loginPage = LoginPage(self.driver)
        loginPage.load()
        loginPage.enterLogin()
        loginPage.enterWrongPassword()
        loginPage.clickLoginButton()
        self.waitElement(loginPage.wrong_cred_window_text)
        wrong_password_text = loginPage.getWrongCredWindowText()
        assert "The password you’ve entered is incorrect. Forgot Password?" == wrong_password_text


    @pytest.mark.parametrize("username, passw", [("John", 111), ("Vasyl", 2222)])
    def test_switch_user(self, username, passw):
        loginPage = LoginPage(self.driver)
        loginPage.load()
        loginPage.getLoginField().send_keys(username)
        loginPage.getPasswordField().send_keys(passw)
        login_value = loginPage.getLoginField().get_attribute("value")
        password_value =loginPage.getPasswordField().get_attribute("value")
        assert login_value == username
        assert int(password_value) == passw



'''''
    def test_login_wrong_username(self):
        loginPage = LoginPage(self.driver)
        loginPage.load()
        loginPage.enterWrongLogin()
        loginPage.enterPassword()
        loginPage.clickLoginButton()
        self.waitElement(loginPage.wrong_cred_window_text)
        wrong_cred_text = loginPage.getWrongCredWindowText()
        assert "The password that you've entered is incorrect" in wrong_cred_text
        '''''




































