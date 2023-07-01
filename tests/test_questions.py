import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPageHelper


@allure.title('Проверка раздела «Вопросы о важном»')
@allure.description('Переходим на главную страницу и прокручиваем до блока "Вопросы о важном" и проверяем, что каждый '
                    'из блоков открывается и содержание соответствует ожиданиям')
@pytest.mark.parametrize('acord,textac, val',
                         [[MainPageLocators.LOCATOR_ACCORDION_0, MainPageLocators.LOCATOR_ACCORDION_0_TEXT, 'Сутки'],
                          [MainPageLocators.LOCATOR_ACCORDION_1, MainPageLocators.LOCATOR_ACCORDION_1_TEXT,
                           'покататься'],
                          [MainPageLocators.LOCATOR_ACCORDION_2, MainPageLocators.LOCATOR_ACCORDION_2_TEXT, 'Отсчёт'],
                          [MainPageLocators.LOCATOR_ACCORDION_3, MainPageLocators.LOCATOR_ACCORDION_3_TEXT,
                           'расторопнее'],
                          [MainPageLocators.LOCATOR_ACCORDION_4, MainPageLocators.LOCATOR_ACCORDION_4_TEXT, '1010'],
                          [MainPageLocators.LOCATOR_ACCORDION_5, MainPageLocators.LOCATOR_ACCORDION_5_TEXT,
                           'передышек'],
                          [MainPageLocators.LOCATOR_ACCORDION_6, MainPageLocators.LOCATOR_ACCORDION_6_TEXT, 'записки'],
                          [MainPageLocators.LOCATOR_ACCORDION_7, MainPageLocators.LOCATOR_ACCORDION_7_TEXT,
                           'самокатов']])
def test_menu_accordions(driver, acord, textac, val):
    main_page = MainPageHelper(driver)
    main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
    main_page.click_on_order_button(2500, acord)
    element = main_page.get_panel(textac)
    assert val in element.text
