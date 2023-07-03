from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPageLocators:
    LOCATOR_ZAKAZ_HEADER = (By.XPATH, "//button[contains(text(),'Статус заказа')]/preceding-sibling::*")                # Кнопка Заказать в начале страницы
    LOCATOR_ZAKAZ_DOWN = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[1]")                               # Кнопка Заказать в конце страницы
    LOCATOR_ACCORDION_0 = (By.XPATH, "//div[@id='accordion__heading-0']")                                               # Первый элемент выпадающего списка
    LOCATOR_ACCORDION_1 = (By.XPATH, "//div[@id='accordion__heading-1']")                                               # Второй элемент выпадающего списка
    LOCATOR_ACCORDION_2 = (By.XPATH, "//div[@id='accordion__heading-2']")                                               # Третий элемент выпадающего списка
    LOCATOR_ACCORDION_3 = (By.XPATH, "//div[@id='accordion__heading-3']")                                               # Четвертый элемент выпадающего списка
    LOCATOR_ACCORDION_4 = (By.XPATH, "//div[@id='accordion__heading-4']")                                               # Пятый элемент выпадающего списка
    LOCATOR_ACCORDION_5 = (By.XPATH, "//div[@id='accordion__heading-5']")                                               # Шестой элемент выпадающего списка
    LOCATOR_ACCORDION_6 = (By.XPATH, "//div[@id='accordion__heading-6']")                                               # Седьмой элемент выпадающего списка
    LOCATOR_ACCORDION_7 = (By.XPATH, "//div[@id='accordion__heading-7']")                                               # Восьмой элемент выпадающего списка
    LOCATOR_ACCORDION_0_TEXT = (By.XPATH, "//div[@id='accordion__panel-0']/p")                                          # Содержание выпадающего списка 1 элемента
    LOCATOR_ACCORDION_1_TEXT = (By.XPATH, "//div[@id='accordion__panel-1']/p")                                          # Содержание выпадающего списка 2 элемента
    LOCATOR_ACCORDION_2_TEXT = (By.XPATH, "//div[@id='accordion__panel-2']/p")                                          # Содержание выпадающего списка 3 элемента
    LOCATOR_ACCORDION_3_TEXT = (By.XPATH, "//div[@id='accordion__panel-3']/p")                                          # Содержание выпадающего списка 4 элемента
    LOCATOR_ACCORDION_4_TEXT = (By.XPATH, "//div[@id='accordion__panel-4']/p")                                          # Содержание выпадающего списка 5 элемента
    LOCATOR_ACCORDION_5_TEXT = (By.XPATH, "//div[@id='accordion__panel-5']/p")                                          # Содержание выпадающего списка 6 элемента
    LOCATOR_ACCORDION_6_TEXT = (By.XPATH, "//div[@id='accordion__panel-6']/p")                                          # Содержание выпадающего списка 7 элемента
    LOCATOR_ACCORDION_7_TEXT = (By.XPATH, "//div[@id='accordion__panel-7']/p")                                          # Содержание выпадающего списка 8 элемента