import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators.locators_page_order_scroller import PageOrderLocators
from pages.base_page import BasePage


class OrderScooterPage(BasePage):
    def click_on_order(self, arg):

        self.click_on_button_order(PageOrderLocators.BUTTON_ORDER, arg)

    def enter_name(self, name):
        self.add_text_to_element(PageOrderLocators.NANE_FIELD, name)

    def enter_surname(self, surname):
        self.add_text_to_element(PageOrderLocators.SURNAME_FIELD, surname)

    def enter_address(self, address):
        self.add_text_to_element(PageOrderLocators.ADDRESS_FIELD, address)

    def enter_telephone(self, telephone):
        self.add_text_to_element(PageOrderLocators.TELEPHONE_FIELD, telephone)

    def enter_metro(self, metro):
        locator_metro = PageOrderLocators.metro_locator(metro)
        self.add_text_to_element(PageOrderLocators.METRO_FIELD, metro)
        self.click_on_element(locator_metro)

    def click_on_button_enter_first_page_order(self):
        self.click_on_element(PageOrderLocators.BUTTON_ENTER)

    def enter_when_scooter(self, when_scooter):
        self.add_text_to_element(PageOrderLocators.WHEN_NEED_SCOOTER_FIELD, when_scooter)

    def enter_the_rental_period(self, the_rental_period):
        locator_rental_period = PageOrderLocators.rent_time_locator(the_rental_period)
        self.click_on_element(PageOrderLocators.DROP_DAWN_RENTAL)
        self.click_on_element(locator_rental_period)

    def enter_when_check_box_color(self, check_box_color):
        locator_check_box = PageOrderLocators.check_box_collor_locator(check_box_color)
        self.click_on_element(locator_check_box)

    def enter_comment(self, comment):
        self.add_text_to_element(PageOrderLocators.COMMENT, comment)

    def click_on_button_yes_or_not(self):
        self.click_on_element(PageOrderLocators.BUTTON_YES)


    def click_on_logo_scooter(self):
        self.click_on_element(PageOrderLocators.BUTTON_HEADER_SCOOTER)

    def click_on_logo_dzen(self):
        self.click_on_element(PageOrderLocators.BUTTON_HEADER_DZEN)

    def click_on_look_at_status(self):
        self.click_on_element(PageOrderLocators.BUTTON_LOOK_AT_STATUS)

    def assert_field_yandex(self):
        self.find_element_with_wait(PageOrderLocators.SEARCH_YANDEX_FIELD)




