"""Общие действия для разных тестов для ИМ DNS. """

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
        self.browser.find_element_by_css_selector('.header-top .w-choose-city-widget-label i').click()

        # Ожидаем появления поля для ввода текста не более 5 мин
        find_city = WebDriverWait(self.browser, BROWSER_TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Найти город"]'))
        )

        # Вводим в поле города "Ростов-на-Дону"
        find_city.send_keys('Ростов-на-Дону')

        # В выпадающем списке кликаем на г.Ростов-на-Дону
        choice = self.browser.find_element_by_css_selector('.cities-search '
                                                           'a[data-city-id="9437a276-5970-11de-8bf7-00151716f9f5"]')
        choice.click()

        # Проверяем что выбран город Ростов-на-Дону
        city = self.browser.find_element_by_css_selector('.header-top .w-choose-city-widget-label').text
        if city != 'Ростов-на-Дону':
            raise InvalidElementValue('Ожидается Ростов-на-Дону. Выбран другой город.')
