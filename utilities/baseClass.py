import pytest

from pageObjects.FacebookLoginPage import FacebookLoginPage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getNewLink(self, linkText):
        loginPage = FacebookLoginPage()
        self.driver.get(linkText)
        return loginPage


