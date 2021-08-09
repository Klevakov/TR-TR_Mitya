"""Тесты корзины"""
import time

from common import CommonActions
from core import TestBase
from exceptions import InvalidElementValue


class CartPageTest(TestBase, CommonActions):
    """Набор тестов для корзины. """

    def test_removing_product_from_cart(self):
        """Тест удаления товара из корзины. """

        # Переключаем город на Ростов-на-Дону.
        self.change_city_to_rostov()

        # Тестируем на разделе "Смартфоны и гаджеты -> Смартфоны"
        directory_selector = 'a[href="/catalog/17a890dc16404e77/smartfony-planshety-i-fototexnika/"]'
        subdirectory_selector = 'a[href="/catalog/17a8a01d16404e77/smartfony/"]'
        self.go_to_subdirectory(directory_selector, subdirectory_selector)

        # На первом товаре нажимаем "Купить"
        self.click_to_first_element('.buy-btn')

        # Кликаем на Корзину
        self.check_and_click('.buttons .cart-link')

        # В корзине под полем с товаром нажимаем “Удалить”
        self.find_element_by_css_and_text('button[class="menu-control-button"]', 'Удалить').click()
        time.sleep(3)

        # Проверяем, что в корзине не осталось товаров
        count = self.find_by_css('.buttons .cart-link__badge').text
        if count:
            raise InvalidElementValue('Корзина не пуста')
