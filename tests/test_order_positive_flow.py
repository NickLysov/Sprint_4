import pytest
import allure

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPageHelper
from pages.order_page import OrderPageHelpers


@allure.title('Позитивный сценарий оформления заказа')
@allure.description(
    'Проверка позитивного сценария оформления заказа и перехода после этого на главную страницу, переход по ссылке  яндекса')
@pytest.mark.parametrize('scroll,btn',
                         [[2, MainPageLocators.LOCATOR_ZAKAZ_HEADER], [2500, MainPageLocators.LOCATOR_ZAKAZ_DOWN]])
def test_order_create(driver, scroll, btn):
    main_page = MainPageHelper(driver)
    main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
    order_page = OrderPageHelpers(driver)
    main_page.click_on_order_button(scroll, btn)
    order_page.fill_order_form()
    order_page.click_next()
    element = order_page.get_panel()
    assert 'Запишите его' in element.text

@allure.title('Проверка перехода на главную со страницы заказа')
def test_main_page(driver):
    main_page = MainPageHelper(driver)
    main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
    order_page = OrderPageHelpers(driver)
    main_page.click_on_order_button(2, MainPageLocators.LOCATOR_ZAKAZ_HEADER)
    samokat = order_page.open_samokat()
    assert 'https://qa-scooter.praktikum-services.ru/' == samokat, "Переход не осуществлен на главную https://qa-scooter.praktikum-services.ru/"

@allure.title('Проверка ссылки из хедера по логотипу Яндекс')
def test_ya_link(driver):
    main_page = MainPageHelper(driver)
    main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
    order_page = OrderPageHelpers(driver)
    main_page.click_on_order_button(2, MainPageLocators.LOCATOR_ZAKAZ_HEADER)
    new_page = order_page.open_ya()
    assert 'yandex.ru' in new_page, "Переход не осуществлен на yandex.ru, открылся иной url"
