from selenium.webdriver.common.by import By

from utilities.TestData import TestData


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    URL = "https://www.facebook.com"
    login_field = (By.ID, "email")
    password_field = (By.ID, "pass")
    login_button = (By.NAME, "login")
    wrong_cred_window_text = (By.CLASS_NAME, "_9ay7")


    def load(self):
        self.driver.get(self.URL)

    def getPageTitle(self):
        title = self.driver.title
        return title

    def enterLogin(self):
        self.driver.find_element(*self.login_field).send_keys(TestData.login)

    def enterPassword(self):
        self.driver.find_element(*LoginPage.password_field).send_keys(TestData.password)

    def clickLoginButton(self):
        self.driver.find_element(*LoginPage.login_button).click()

    def enterWrongLogin(self):
        self.driver.find_element(*self.login_field).send_keys(TestData.wrong_login)

    def enterWrongPassword(self):
        self.driver.find_element(*LoginPage.password_field).send_keys(TestData.wrong_password)

    def getWrongCredWindowText(self):
        return self.driver.find_element(*self.wrong_cred_window_text).text






















