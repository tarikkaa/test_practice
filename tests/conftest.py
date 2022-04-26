import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.config import Config

driver = None

pytest_plugins = [
   "tests.fixtures.fixtures_try"
  ]

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='choose the browser: --chrome or --firefox')
    parser.addoption('--env', action='store', default='windows', help='choose current OS: --windows or --mac')

@pytest.fixture(scope='class')
def getOS(request):
    env = request.config.getoption("--env")
    return env

@pytest.fixture(scope='class')
def setOS(getOS):
    os = Config(getOS)
    return os

@pytest.fixture(scope='class')
def setup(request, setOS):
    global driver
    browser = request.config.getoption('browser')
    if browser == "chrome":
        s = Service(setOS.chrome_driver)
        driver = webdriver.Chrome(service=s)
    elif browser == "firefox":
        s = Service(setOS.firefox_driver)
        driver = webdriver.Firefox(service=s)
    else:
        raise Exception("Unsupported browser")
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.close()












