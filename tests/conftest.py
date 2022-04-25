import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None



''''
@pytest.fixture(scope="class")
def setup(request):
    global driver
    #s = Service("/Users/tar/Drivers/chromedriver")
    s = Service("C:\\ChromeDriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.close()
'''


def pytest_addoption_browser(parser):
    parser.addoption('--browser', action='store', default='chrome', help='choose the browser: --chrome or --firefox')

@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser = request.config.getoption('browser')
    if browser == "chrome":
        s = Service("C:\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser == "firefox":
        s = Service("C:\\firefoxDriver\\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    else:
        raise Exception("Unsupported browser")

    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.close()

'''
@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def set_driver(env):
    config = Config(env)
    return config
'''









