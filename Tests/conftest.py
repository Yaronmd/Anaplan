import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

MAIN_URL = "https://predictive.anaplan.com/"

@pytest.fixture(scope='class')
def init_driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(MAIN_URL)
    driver.maximize_window()
    request.cls.driver = driver
    
    
    yield
    driver.close()

