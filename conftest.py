import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@allure.title('Цикл запуска браузера и его выгрузки после выполнения тестов')
@allure.description('Задаем параметры запуска браузера и выход из него после')
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
