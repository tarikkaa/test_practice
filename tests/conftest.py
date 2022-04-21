import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    global driver
    #driver = webdriver.Chrome(executable_path='/Users/tar/Drivers/chromedriver')
    #driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
    #s = Service("/Users/tar/Drivers/chromedriver")
    s = Service("C:\\ChromeDriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    request.cls.driver = driver
    driver.maximize_window()

    yield
    driver.close()








