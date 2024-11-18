import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_page_order_scroller import PageOrderLocators
import time

from pages.page_order_scooter import OrderScooterPage
from urls import UrelsSamokati


class TestQuestionText:

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Firefox(options=options)

    @pytest.mark.parametrize('name, surname, address, metro, telephone, when_scooter,the_rental_period, check_box_color, comment, arg', [
        (["Илья"], ["Тутович"], ["Кострома"], ["Преображенская площадь"], ["899923412345"], ["15"], ["сутки"], ["black"], ["Прям ща"],0),
        (["Иван"], ["Иванов"], ["Владивосток"], ["Красносельская"], ["890090000011"], ["16"], ["двое суток"], ["grey"], ["Вчера"], 1)
    ])
    def test_filling_order_form(self, name, surname, address, metro, telephone, when_scooter,the_rental_period, check_box_color, comment, arg):

        self.driver.get(UrelsSamokati.BASE_URL)
        click_order_button = OrderScooterPage(self.driver)
        click_order_button.click_on_button_order(arg)
        click_order_button.enter_name(name)
        click_order_button.enter_surname(surname)
        click_order_button.enter_address(address)
        click_order_button.enter_metro(metro)
        click_order_button.enter_telephone(telephone)
        click_order_button.click_on_button_enter_first_page_order()
        click_order_button.enter_when_scooter(when_scooter)
        click_order_button.enter_when_check_box_color(check_box_color)
        click_order_button.enter_the_rental_period(the_rental_period)
        click_order_button.enter_comment(comment)
        click_order_button.click_on_button_order(1)
        click_order_button.click_on_button_yes_or_not()
        time.sleep(1)
        header_to_check_text = self.driver.find_element(*PageOrderLocators.ASSERT_CHECK_TEXT_ORDER_COMPLETE)
        assert "Заказ оформлен" in header_to_check_text.text

        click_order_button.click_on_look_at_status()
        click_order_button.click_on_logo_scooter()
        time.sleep(2)
        expected_url_scoot = UrelsSamokati.expected_url_scooter
        current_url = self.driver.current_url
        assert current_url == expected_url_scoot

        click_order_button.click_on_logo_dzen()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_url = UrelsSamokati.expected_url_dzen
        current_url = self.driver.current_url
        assert current_url == expected_url



    @classmethod
    def teardown_class(cls):

        cls.driver.quit()
