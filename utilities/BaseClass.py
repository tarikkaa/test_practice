import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:

    def waitElement(self, locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((locator)))

