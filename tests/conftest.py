import pytest

@pytest.fixture(scope="class")
def setup(request):
    from selenium import webdriver
    #driver = webdriver.Chrome(executable_path='/Users/tar/Drivers/chromedriver')
    driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
    request.cls.driver = driver
    driver.maximize_window()

    yield
    driver.close()



