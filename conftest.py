
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture

def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()