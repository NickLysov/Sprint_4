from locators.order_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPageHelpers(BasePage):
    @allure.step('Поиска локатора и ввод в его поле значения')
    def field_order_entering(self, locator, word):
        search_field = self.find_element_located(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    @allure.step('Поиска локатора и выбор в выпадающем списке значения')
    def field_placeholder_entering(self, locator, field):
        search_field = self.find_element_located(locator)
        search_field.click()
        sh = self.find_element_located(field)
        sh.click()
        return search_field

    @allure.step('Нажатие на кнопку "Далее" при оформлении заказа')
    def click_on_order_button(self):
        return self.find_element_located(OrderPageLocators.LOCATOR_NEXT_PANEL_ORDER, time=2).click()

    @allure.step('Поиск и выбор значения чекбокса')
    def click_checkbox(self, locator):
        return self.find_element_located(locator, time=2).click()

    @allure.step('Находим кнопку подтверждения заказа и кликаем по ней')
    def click_next(self):
        self.find_element_located(OrderPageLocators.LOCATOR_ZAKAZAT_ORDER, time=2).click()
        return self.find_element_located(OrderPageLocators.LOCATOR_CONFIRM_APPRUVE_ORDER, time=2).click()

    @allure.step('Ищем элемент')
    def get_panel(self):
        return self.find_element_located(OrderPageLocators.LOCATOR_FIELD_NUMBER_ORDER)

    @allure.step('Открываем ссылку ведущую на Яндекс и переключаемся на новую вкладку')
    def open_ya(self):
        self.find_element_located(OrderPageLocators.LOCATOR_YA_LINK, time=2).click()
        return str(self.switch_window())

    @allure.step('Переход к на главную по кнопке самокат в заголовке')
    def open_samokat(self):
        self.find_element_located(OrderPageLocators.LOCATOR_CHECK_BUTTON_ORDER, time=2).click()
        self.find_element_located(OrderPageLocators.LOCATOR_SAMOKAT_LINK, time=2).click()
        return str(self.check_url())
