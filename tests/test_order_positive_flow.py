import pytest
import allure

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPageHelper, get_name, get_last_name, get_address, get_phone_number
from locators.order_locators import OrderPageLocators
from pages.order_page import OrderPageHelpers


@allure.title('Позитивный сценарий оформления заказа')
@allure.description(
    'Проверка позитивного сценария оформления заказа и перехода после этого на главную страницу, переход по ссылке яндекса')
@pytest.mark.parametrize('scroll,btn',
                         [[2, MainPageLocators.LOCATOR_ZAKAZ_HEADER], [2500, MainPageLocators.LOCATOR_ZAKAZ_DOWN]])
def test_order_create(driver, scroll, btn):
    main_page = MainPageHelper(driver)
    main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
    order_page = OrderPageHelpers(driver)
    main_page.click_on_order_button(scroll, btn)
    order_page.field_order_entering(OrderPageLocators.LOCATOR_NAME_FIELD_ORDER, get_name())
    order_page.field_order_entering(OrderPageLocators.LOCATOR_SURNAME_FIELD_ORDER, get_last_name())
    order_page.field_order_entering(OrderPageLocators.LOCATOR_ADDRESS_FIELD_ORDER, get_address())
    order_page.field_placeholder_entering(OrderPageLocators.LOCATOR_METRO_FIELD_ORDER,
                                          OrderPageLocators.LOCATOR_SEARCH_SELECT)
    order_page.field_order_entering(OrderPageLocators.LOCATOR_TNUMBER_FIELD_ORDER, get_phone_number())
    order_page.click_on_order_button()
    order_page.field_placeholder_entering(OrderPageLocators.LOCATOR_DATA_FIELD_ORDER,
                                          OrderPageLocators.LOCATOR_CALENDAR_FIELD_ORDER)
    order_page.field_placeholder_entering(OrderPageLocators.LOCATOR_ARENDA_FIELD_ORDER,
                                          OrderPageLocators.LOCATOR_TERM_SELECT)
    order_page.click_checkbox(OrderPageLocators.LOCATOR_GREY_COLOR_ORDER)
    order_page.field_order_entering(OrderPageLocators.LOCATOR_COMMENT_FIELD_ORDER, 'Комментариев нет')
    order_page.click_next()
    element = order_page.get_panel()
    assert 'Запишите его' in element.text
    samokat = order_page.open_samokat()
    assert 'https://qa-scooter.praktikum-services.ru/' == samokat, "Переход не осуществлен на главную " \
                                                                   "https://qa-scooter.praktikum-services.ru/"
    new_page = order_page.open_ya()
    assert 'yandex.ru' in new_page, "Переход не осуществлен на yandex.ru, открылся иной url"
