import allure
from faker import Faker

from pages.base_page import BasePage

fake = Faker("ru_RU")


def get_name():
    name = fake.first_name()
    return name


def get_last_name():
    last_name = fake.last_name()
    return last_name


def get_address():
    address = fake.street_address()
    return address


def get_phone_number():
    phone_number = fake.numerify(text='+7%%%%%%%%%%')
    return phone_number


class MainPageHelper(BasePage):
    @allure.title('Прокрутка страницы до кнопки заказа')
    @allure.description('Скроллим страницу на {scroll} пикселей и жмем кнопку Заказать')
    def click_on_order_button(self, scroll, btn):
        self.scroll_window(scroll)
        return self.find_element_located(btn, time=2).click()

    @allure.step('Ищем элемент {ele}')
    def get_panel(self, ele):
        return self.find_element_located(ele)
