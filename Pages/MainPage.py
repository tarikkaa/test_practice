from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//span[contains(text(), 'John Lucky')]")
    account_button = (By.XPATH, "//div[@aria-label='Your profile']")
    logout_button = (By.XPATH, "//span[contains(text(),'Log Out')]")

    def getUsername(self):
        username = self.driver.find_element(*self.username).text
        return username

    def gotoAccountSection(self):
        self.driver.find_element(*self.account_button).click()

    def logOut(self):
        self.driver.find_element(*self.logout_button).click()


