from selenium.webdriver.common.by import By

from utilities.TestData import TestData


class FacebookLoginPage:
    def __init__(self, driver):
        self.driver = driver

    login_field = (By.ID, "email")
    password_field = (By.ID, "pass")
    login_button = (By.NAME, "login")
    main_page_user = (By.XPATH, "//span[contains(text(), 'John Lucky')]")


    def enterLogin(self):
        self.driver.find_element(*FacebookLoginPage.login_field).send_keys(TestData.login)

    def enterPassword(self):
        self.driver.find_element(*FacebookLoginPage.password_field).send_keys(TestData.password)

    def clickLoginButton(self):
        self.driver.find_element(*FacebookLoginPage.login_button).click()

    def getMainPageUser(self):
        user = self.driver.find_element(*FacebookLoginPage.main_page_user).text
        return user
















