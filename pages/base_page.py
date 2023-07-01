import time
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {base_url}')
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    @allure.step('Ищем элемент {locator}')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not find {locator}')

    @allure.title('Меняем рабочую вкладку')
    @allure.description('Переключаемся на вторую вкладку и возвращаем её url')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        return self.driver.current_url

    @allure.step('Проверяем URl текущей страницы')
    def check_url(self):
        time.sleep(5)
        return self.driver.current_url

    @allure.title('Прокрутка страницы')
    @allure.description('Скроллим страницу на {scroll} пикселей')
    def scroll_window(self, scroll):
        scroll_by = f'window.scrollBy(0, {scroll});'
        self.driver.execute_script(scroll_by)
        time.sleep(3)
        return self.driver
