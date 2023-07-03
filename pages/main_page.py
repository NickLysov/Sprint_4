import allure

from pages.base_page import BasePage

class MainPageHelper(BasePage):
    @allure.title('Прокрутка страницы до кнопки заказа')
    @allure.description('Скроллим страницу на {scroll} пикселей и жмем кнопку Заказать')
    def click_on_order_button(self, scroll, btn):
        self.scroll_window(scroll,btn)
        return self.find_element_located(btn, time=2).click()

    @allure.step('Ищем элемент {ele}')
    def get_panel(self, ele):
        return self.find_element_located(ele)
