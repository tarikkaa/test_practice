import time

import pytest
from selenium import webdriver
driver = None

@pytest.fixture(scope="class")
def setup():
    global driver
    driver = webdriver.Chrome(executable_path='/Users/tar/Drivers/chromedriver')
    driver.maximize_window()
    yield
    time.sleep(3)
    driver.close()
