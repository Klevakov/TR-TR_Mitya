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

        # Добавляем товар и переходим в корзину
        self.add_product_to_cart()

        # В корзине под полем с товаром нажимаем “Удалить”
        self.find_element_by_css_and_text('button[class="menu-control-button"]', 'Удалить').click()
        time.sleep(3)

        # Проверяем, что в корзине не осталось товаров
        count = self.find_by_css('.buttons .cart-link__badge').text
        if count:
            raise InvalidElementValue('Корзина не пуста')

    def test_change_quantity_product(self):
        """Тест изменения количества товара **в корзине**. """

        # Добавляем товар и переходим в корзину
        self.add_product_to_cart()

        # Запоминаем цену одной единицы товара
        price1 = self.find_by_css('.cart-items__content-container .price__current').text
        price1 = int(''.join(price1.split())[:-1])

        # Увеличиваем количество товара на 1
        self.check_and_click('.count-buttons__icon-plus')

        # Ждем, пока счетчик товара не изменится на '2'
        for i in range(60):
            count = self.find_by_css('.total-amount__count').text
            count = int(count.strip().split()[1])
            if count == 2:
                break
            time.sleep(1)

        # Запоминаем цену двух единиц товара
        price2 = self.find_by_css('.cart-items__content-container .price__current').text
        price2 = int(''.join(price2.split())[:-1])

        # Проверяем рассчитанную цену
        assert price1 * count == price2

        # Уменьшаем количество товара на 1
        self.check_and_click('.count-buttons__icon-minus')

        # Ждем, пока счетчик товара не изменится на '1'
        for i in range(60):
            count = self.find_by_css('.total-amount__count').text
            count = int(count.strip().split()[1])
            if count == 1:
                break
            time.sleep(1)

        # Запоминаем цену одной единицы товара
        price = self.find_by_css('.cart-items__content-container .price__current').text
        price = int(''.join(price.split())[:-1])

        # Проверяем рассчитанную цену
        assert price1 * count == price

        # Уменьшаем количество товара на 1
        self.check_and_click('.count-buttons__icon-minus')
        time.sleep(5)

        # Проверяем, что в корзине не осталось товаров
        count = self.find_by_css('.buttons .cart-link__badge').text
        if count:
            raise InvalidElementValue('Корзина не пуста')
