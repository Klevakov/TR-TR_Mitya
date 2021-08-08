"""Тесты корзины"""

from common import CommonActions
from core import TestBase


class CartPageTest(TestBase, CommonActions):
    """Набор тестов для корзины. """

    def test_removing_product_from_cart(self):
        """Тест удаления товара из корзины. """

        # Переключаем город на Ростов-на-Дону.
        self.change_city_to_rostov()
