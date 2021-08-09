"""Конфигурация TR-TR_Mitya. """

import os

# Точка входа - url интернет-магазина
ENTRY_POINT = os.getenv('ENTRY_POINT', 'https://www.dns-shop.ru/')

# Путь к geckodriver
GECKO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'trtr_mitya/driver/geckodriver'))

# Путь к модулям с тестами
TESTS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'trtr_mitya'))

# Время ожидания отклика браузера в минутах
BROWSER_TIMEOUT = int(os.getenv('BROWSER_TIMEOUT', '20'))

TEST = os.getenv('TEST', '')
if TEST:
    TEST = TEST.split(',')
