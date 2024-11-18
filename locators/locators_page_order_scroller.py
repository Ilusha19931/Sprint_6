from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageOrderLocators:
    NANE_FIELD = (By.XPATH, "//input[@placeholder= '* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder= '* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder= '* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder= '* Станция метро']")
    TELEPHONE_FIELD = (By.XPATH, "//input[@placeholder= '* Телефон: на него позвонит курьер']")
    BUTTON_ENTER = (By.XPATH, "//button[text() = 'Далее']")
    WHEN_NEED_SCOOTER_FIELD = (By.XPATH, "//input[@placeholder= '* Когда привезти самокат']")
    DROP_DAWN_RENTAL = (By.XPATH, "//*[text() = '* Срок аренды']")
    COMMENT = (By.XPATH, "//input[@placeholder= 'Комментарий для курьера']")
    BUTTON_YES = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text() = 'Да']")
    BUTTON_ORDER = (By.XPATH, './/button[text()="Заказать"]')
    ASSERT_CHECK_TEXT_ORDER_COMPLETE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    BUTTON_HEADER_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    BUTTON_HEADER_DZEN = (By.XPATH, "//img[@alt='Yandex']")
    BUTTON_LOOK_AT_STATUS = (By.XPATH, "//*[text() = 'Посмотреть статус']")

    @staticmethod
    def metro_locator(metro):
        return By.XPATH, f"//*[contains(text(), '{metro[0]}')]"

    @staticmethod
    def check_box_collor_locator(check_box_color):
        return By.ID, f"{check_box_color[0]}"

    @staticmethod
    def rent_time_locator(the_rental_period):
        return By.XPATH, f"//div[text() = '{the_rental_period[0]}']"
