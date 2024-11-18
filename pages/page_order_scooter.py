import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_page_order_scroller import PageOrderLocators


class OrderScooterPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_button_order(self, arg):

        button_order = self.driver.find_elements(*PageOrderLocators.BUTTON_ORDER)
        self.driver.execute_script(f"arguments[0].scrollIntoView();", button_order[arg])
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(PageOrderLocators.BUTTON_ORDER))
        button_order[arg].click()

    def enter_name(self, name):

        self.driver.find_element(*PageOrderLocators.NANE_FIELD).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element(*PageOrderLocators.SURNAME_FIELD).send_keys(surname)

    def enter_address(self, address):
        self.driver.find_element(*PageOrderLocators.ADDRESS_FIELD).send_keys(address)

    def enter_telephone(self, telephone):
        self.driver.find_element(*PageOrderLocators.TELEPHONE_FIELD).send_keys(telephone)

    def enter_metro(self, metro):
        self.driver.find_element(*PageOrderLocators.METRO_FIELD).send_keys(metro)
        time.sleep(0.2)
        self.driver.find_element(*PageOrderLocators.metro_locator(metro)).click()

    def click_on_button_enter_first_page_order(self):
        time.sleep(0.2)
        self.driver.find_element(*PageOrderLocators.BUTTON_ENTER).click()

    def enter_when_scooter(self, when_scooter):
        self.driver.find_element(*PageOrderLocators.WHEN_NEED_SCOOTER_FIELD).send_keys(when_scooter)
        time.sleep(0.2)

    def enter_the_rental_period(self, the_rental_period):
        self.driver.find_element(*PageOrderLocators.DROP_DAWN_RENTAL).click()
        self.driver.find_element(*PageOrderLocators.rent_time_locator(the_rental_period)).click()
        time.sleep(0.2)

    def enter_when_check_box_color(self, check_box_color):
        self.driver.find_element(*PageOrderLocators.check_box_collor_locator(check_box_color)).click()
        time.sleep(0.2)

    def enter_comment(self, comment):
        self.driver.find_element(*PageOrderLocators.COMMENT).send_keys(comment)
        time.sleep(0.2)

    def click_on_button_yes_or_not(self):
        button_yes = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(PageOrderLocators.BUTTON_YES))
        button_yes.click()

    def click_on_logo_scooter(self):
        self.driver.find_element(*PageOrderLocators.BUTTON_HEADER_SCOOTER).click()

    def click_on_logo_dzen(self):
        self.driver.find_element(*PageOrderLocators.BUTTON_HEADER_DZEN).click()

    def click_on_look_at_status(self):
        self.driver.find_element(*PageOrderLocators.BUTTON_LOOK_AT_STATUS).click()




