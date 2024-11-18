import pytest
from selenium import webdriver
from pages.main_page_question import MainPageQuestion
import time

from urls import UrelsSamokati


class TestQuestionText:

    @classmethod
    def setup_class(cls):

        cls.driver = webdriver.Chrome()


    @pytest.mark.parametrize('index, expected_words', [
            (0, ["Сутки — 400 рублей. Оплата курьеру — наличными или картой."]),
            (1, ["Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]),
            (2, ["Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]),
            (3, ["Только начиная с завтрашнего дня. Но скоро станем расторопнее."]),
            (4, ["Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]),
            (5, ["Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]),
            (6, ["Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]),
            (7, ["Да, обязательно. Всем самокатов! И Москве, и Московской области."])])

    def test_text_in_object_1(self, index, expected_words):


        self.driver.get(UrelsSamokati.BASE_URL)
        scroll_to_element = MainPageQuestion(self.driver)

        scroll_to_element.scroll_to_last_question()
        scroll_to_element.click_question_form(index)
        time.sleep(0.3)

        actual_text = scroll_to_element.text_on_assert(index)
        for word in expected_words:
            assert word in actual_text



    @classmethod
    def teardown_class(cls):

        cls.driver.quit()

