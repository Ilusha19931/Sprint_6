
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_main_page_question import MainPageLocators
from locators.locators_page_order_scroller import PageOrderLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_the_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.find_element_with_wait(locator).click()

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return element.text


    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def skroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locators(self, locator_question, index):
        method, locator = locator_question
        locator = locator.format(index)
        return (method, locator)

    def click_on_button_order(self,locator, arg):

        button_order = self.driver.find_elements(*locator)
        button_order_arg = button_order[arg]
        self.driver.execute_script("arguments[0].scrollIntoView();", button_order_arg)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        button_order_arg.click()


