from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//span[contains(text(), 'John Lucky')]")


    def getUsername(self):
        username = self.driver.find_element(*self.username).text
        return username