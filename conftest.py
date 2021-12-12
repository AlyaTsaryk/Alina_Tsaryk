import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def browser():
    s = Service('./chromedriver.exe')
    driver = webdriver.Chrome(
        service=s
    )
    yield driver
    driver.close()