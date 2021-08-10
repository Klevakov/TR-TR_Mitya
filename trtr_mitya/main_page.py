"""Тесты главной страницы интернет-магазина. """

from trtr_mitya.core import TestBase
from trtr_mitya.common import CommonActions


class MainPageTest(TestBase, CommonActions):
    """Набор тестов для главной интернет-магазина. """

    def test_choosing_city(self):
        """Тест ручного выбора города. """

        # Вручную изменяем город на Ростов-на-Дону и проверяем что город изменился
        self.change_city('Ростов-на-Дону')

        # Вручную изменяем город на Краснодар и проверяем что город изменился
        self.change_city('Краснодар')

        # Вручную изменяем город на Волгодонск и проверяем что город изменился
        self.change_city('Волгодонск')
