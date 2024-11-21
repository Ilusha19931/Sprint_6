from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MainPageLocators:
    BUTTON_WITH_QUESTION = (By.XPATH, "//*[@id='accordion__heading-{}']")
    QUESTION_TEXT = (By.XPATH, "//*[@id='accordion__panel-{}']")
    QUESTION_LOCKATOR_TO_SCROLL = (By.XPATH, "//*[@id='accordion__heading-7']")
