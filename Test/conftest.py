import pytest
from selenium import webdriver
from config.config import Testdata


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=Testdata.Chrome_Executable_Path)
    request.cls.driver = web_driver
    yield
    web_driver.close()
