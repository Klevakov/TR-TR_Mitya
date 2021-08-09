"""Общие действия для разных тестов для ИМ DNS. """
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.settings import BROWSER_TIMEOUT
from exceptions import InvalidElementValue


class CommonActions:
    """Набор общих действий, которые используются в разных тестах для ИМ DNS. """

    def change_city_to_rostov(self):
        """Переключает на Ростов-на-Дону. """

        # Нажимаем на ссылку изменения геопозиции
        self.find_by_css('.header-top .w-choose-city-widget-label i').click()

        # Ожидаем появления поля для ввода текста не более 5 мин
        find_city = self.wait_for_visible_element('input[placeholder="Найти город"]')

        # Вводим в поле города "Ростов-на-Дону"
        find_city.send_keys('Ростов-на-Дону')
        time.sleep(2)

        # В выпадающем списке кликаем на г.Ростов-на-Дону
        choice = self.wait_for_element_clickable(
            '.cities-search a[data-city-id="9437a276-5970-11de-8bf7-00151716f9f5"]'
        )
        choice.click()
        time.sleep(5)

        # Проверяем что выбран город Ростов-на-Дону
        city = self.find_by_css('.header-top .w-choose-city-widget-label').text
        if city != 'Ростов-на-Дону':
            raise InvalidElementValue('Ожидается Ростов-на-Дону. Выбран другой город.')

    def add_product_to_cart(self):
        """Добавляет товар и переходит в корзину. """

        # Тестируем на разделе "Смартфоны и гаджеты -> Смартфоны"
        directory_selector = 'a[href="/catalog/17a890dc16404e77/smartfony-planshety-i-fototexnika/"]'
        subdirectory_selector = 'a[href="/catalog/17a8a01d16404e77/smartfony/"]'
        self.go_to_subdirectory(directory_selector, subdirectory_selector)

        # На первом товаре нажимаем "Купить"
        self.click_to_first_element('.buy-btn')

        # Кликаем на Корзину
        self.check_and_click('.buttons .cart-link')

        # Убеждаемся, что мы перешли на страницу корзины
        assert self.find_element_by_css_and_text('.cart-title', 'Корзина')
