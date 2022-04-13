import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    #driver = webdriver.Chrome(executable_path='/Users/tar/Drivers/chromedriver')
    driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()
