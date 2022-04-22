import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getPageTitle(self):
        title = self.driver.title
        return title

    def waitPageTitle(self, page_title):
        WebDriverWait(self.driver, 10).until(EC.title_is(page_title))

    def waitElement(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator)))

