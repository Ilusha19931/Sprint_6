from operator import index
from tkinter.messagebox import QUESTION

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_main_page_question import MainPageLocators
from pages.base_page import BasePage


class MainPageQuestion(BasePage):

    def get_text_assert(self, num):
        locator_question_to_click_formated = self.format_locators(MainPageLocators.BUTTON_WITH_QUESTION, num)
        locator_question_text_formated = self.format_locators(MainPageLocators.QUESTION_TEXT, num)
        self.skroll_to_element(MainPageLocators.QUESTION_LOCKATOR_TO_SCROLL)
        self.click_on_element(locator_question_to_click_formated)
        return self.get_text(locator_question_text_formated)





