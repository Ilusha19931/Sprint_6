from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPageQuestion:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_last_question(self):

        button_with_question = (By.CLASS_NAME, "accordion__heading")
        element = self.driver.find_elements(*button_with_question)[7]
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question_form(self, index):

        button_with_question = (By.CLASS_NAME, "accordion__heading")
        self.driver.find_elements(*button_with_question)[index].click()


    def text_on_assert(self, index):
        text_inside_the_button = (By.XPATH, ".//p")
        text = self.driver.find_elements(*text_inside_the_button)[index]
        return text.text





