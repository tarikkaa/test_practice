import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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











