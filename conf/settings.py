"""Конфигурация TR-TR_Mitya. """

import os
from dotenv import load_dotenv

load_dotenv()  # берет переменные среды из .env файла.

# Точка входа - url интернет-магазина
ENTRY_POINT = os.getenv('ENTRY_POINT', 'https://www.dns-shop.ru/')

# Путь к geckodriver
GECKO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          '..', 'trtr_mitya/driver/geckodriver'))

# Путь к модулям с тестами
TESTS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'trtr_mitya'))

# Путь к .env файлу
DOTENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conf/.env'))

# Количество попыток провести тест
MAX_RETRIES = int(os.getenv('MAX_RETRIES', '5'))

# Время ожидания подгрузки элемента в секундах
WAIT_ELEMENT = int(os.getenv('WAIT_ELEMENT', '15'))

# Максимальноеколичество попыток получить нужный элемент
MAX_NUMBERS_of_ATTEMPTS = int(os.getenv('MAX_NUMBERS_of_ATTEMPTS', '10'))

# Максимальное время на выполнение одного теста в минутах
BROWSER_TIMEOUT = int(os.getenv('BROWSER_TIMEOUT', '5'))

TEST = os.getenv('TEST', '')
if TEST:
    TEST = TEST.split(',')

PASSWORD = os.getenv('PASSWORD')
EMAIL = os.getenv('EMAIL')