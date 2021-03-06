"""Общие действия для разных тестов для ИМ DNS. """
import time

from selenium.common.exceptions import TimeoutException

from conf.settings import MAX_NUMBERS_of_ATTEMPTS
from .exceptions import InvalidElementValue


class CommonActions:  # pylint: disable=E1101
    """Набор общих действий, которые используются в разных тестах для ИМ DNS. """

    def change_city(self, city: str):
        """Переключает на Ростов-на-Дону. """

        # Нажимаем на ссылку изменения геопозиции
        self.find_by_css('.header-top .w-choose-city-widget-label i').click()

        # Ожидаем появления поля для ввода текста не более 5 мин
        find_city = self.wait_for_visible_element('input[placeholder="Найти город"]')

        for _ in range(MAX_NUMBERS_of_ATTEMPTS):
            try:
                # Вводим название города
                find_city.send_keys(city)

                # Перепроверяем варианты раскрывающегося списка
                # на совпадение с названием искомого города
                choice = self.wait_for_elements('.cities-search span')
            except TimeoutException:
                continue
            else:
                break

        for town in choice:
            if town.text.split('\n')[0].strip() == city:
                town.click()
                break

        # Проверяем что выбран верный город
        for _ in range(MAX_NUMBERS_of_ATTEMPTS):
            curent_city = self.find_by_css('.header-top .w-choose-city-widget-label').text
            if curent_city == city:
                break
            time.sleep(2)

        if curent_city != city:
            raise InvalidElementValue('Ожидается {}. Выбран другой город.'.format(city))

    def add_product_to_cart(self):
        """Добавляет товар и переходит в корзину. """

        # Тестируем на разделе "Смартфоны и гаджеты -> Смартфоны"
        directory_selector = ('a[href="/catalog/17a890dc16404e77/'
                              'smartfony-planshety-i-fototexnika/"]')
        subdirectory_selector = 'a[href="/catalog/17a8a01d16404e77/smartfony/"]'

        # Переходим в подкаталог "Смартфоны"
        self.go_to_subdirectory(directory_selector, subdirectory_selector)

        # На первом товаре нажимаем "Купить"
        self.click_to_first_element('.buy-btn')

        # Кликаем на Корзину
        self.check_and_click('.buttons .cart-link')

        # Убеждаемся, что мы перешли на страницу корзины
        assert self.find_element_by_css_and_text('.cart-title', 'Корзина')
