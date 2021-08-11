"""Ядро TR-TR_Mitya. """

import importlib
import inspect
import pkgutil
import traceback

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.settings import ENTRY_POINT, GECKO_PATH, MAX_RETRIES, TEST, TESTS_PATH, WAIT_ELEMENT


class OrderedClass(type):
    """Метакласс для производства классов. """

    @classmethod
    def __prepare__(cls, _name, _bases):
        # Возвращает словарь, ключи которого представляют упорядоченное пространство имен класса
        # и их значения
        return dict()

    def __new__(cls, name, bases, classdict):
        # Создаем атрибут класса со списком атрибутов
        classdict['__ordered__'] = [key for key in classdict.keys()]
        return type.__new__(cls, name, bases, classdict)


class TestBase(metaclass=OrderedClass):
    """Базовый класс для всех тестов тестов. """

    def __init__(self):
        self.browser = None
        self._tests = []

        # Заполняем список тестов
        for method in self.__ordered__:
            if method.startswith('test_'):
                self._tests.append(getattr(self, method))

    def _start_browser(self):
        """Настраивает и запускает браузер на стартовой страничке ИМ. """

        profile = webdriver.FirefoxProfile()

        # Прописываем в настройки браузера - отказ от предоставления геопозиции
        profile.set_preference("geo.enabled", False)
        self.browser = webdriver.Firefox(executable_path=GECKO_PATH, firefox_profile=profile)

        # Открываем стартовую страничку ИМ
        self.browser.get(ENTRY_POINT)

    def run(self):
        """Запускает все тесты один за другим. """

        # Запускаем тесты ис списка тестов по-очереди
        for test in self._tests:
            # Выводим название текущего теста
            description = test.__doc__
            out_white("{}" .format(f'Запускаю "{description}":', end=' '))

            for i in range(MAX_RETRIES):
                # Запускаем тест
                try:
                    self._start_browser()
                    test()
                # Отлавливаем исключения
                except BaseException as e:
                    # Выводим сообщение об исключении на экран
                    out_grey(f'{i+1} - я попытка неудачная. Ошибка:\n' + traceback.format_exc())
                    self.browser.quit()

                    # Если попытки исчерпаны - выводим сообщение о провале
                    if i == MAX_RETRIES - 1:
                        out_red(f'Провал! \n {repr(e)} \n')
                else:
                    self.browser.quit()
                    # Выводим сообщение об успехе
                    out_green('Успех!')
                    break

    def find_by_css(self, selector):
        """Shortcut для поиска элемента по CSS-селектору. """

        return self.browser.find_element_by_css_selector(selector)

    def wait_for_visible_element(self, selector):
        """Ждет пока элемент станет видимым. """

        element = WebDriverWait(self.browser, WAIT_ELEMENT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )
        return element

    def wait_for_element_clickable(self, selector):
        """Ждет пока на элемент можно будет кликнуть. """

        element = WebDriverWait(self.browser, WAIT_ELEMENT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        return element

    def wait_for_elements(self, selector):
        """Ждет пока на подгрузится список элементов, видимых на странице. """

        elements = WebDriverWait(self.browser, WAIT_ELEMENT).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )
        return elements

    def check_by_css(self, selector):
        """Проверяет по CSS-селектору, существует ли элемент. """

        return self.browser.is_element_present_by_css(selector)

    def check_and_click(self, selector):
        """Проверяет по CSS-селектору, существует ли элемент и кликает на него. """

        element = self.find_by_css(selector)
        assert element
        element.click()

    def go_to_subdirectory(self, directory_selector, subdirectory_selector):
        """Переходит из меню в подкаталог. """

        # Наводим мышь на ссылку каталога
        directory_elem = self.wait_for_element_clickable(directory_selector)
        hover_mouse = ActionChains(self.browser)
        hover_mouse.move_to_element(directory_elem).perform()

        # Кликаем на ссылку подкаталога
        subdirectory_elem = self.wait_for_element_clickable(subdirectory_selector)
        subdirectory_elem.click()

    def find_element_by_css_and_text(self, selector, text: str):
        """
        Находит список элементов по селектору и возвращает тот,
        у которого соответствует текст.
        """

        elem_list = self.wait_for_elements(selector)
        for elem in elem_list:
            if elem.text.strip() == text:
                return elem

    def click_to_first_element(self, selector):
        """Находит список элементов по селектору и кликает на первый элемент. """

        elem_list = self.wait_for_elements(selector)
        elem_list[0].click()


def get_tests():
    """Возвращает список тестов. """

    # Создаем пустое пустое множество для наименований тестов
    tests = set()
    # Перебираем названия
    # pkgutil.iter_modules([TESTS_PATH]) - возвращает кортеж из трех переменных:
    # путь к модулю, название модуля и булевское значение
    for _, module_name, _ in pkgutil.iter_modules([TESTS_PATH]):
        # Передаем в переменную объект - модуль
        mod = importlib.import_module(f'trtr_mitya.{module_name}')
        # Перебираем список из кортежей (название класса, объект класса)
        for cls_name, obj in inspect.getmembers(mod):
            if cls_name.endswith('Test') and inspect.isclass(obj):
                if TEST:
                    if cls_name in TEST:
                        tests.add(obj)
                    continue
                tests.add(obj)
    return list(tests)


def run(*args):
    """Запускает тесты. """

    for test_class in args:
        test = test_class()
        test.run()


def out_red(text):
    """Выводит в консоль сообщение красным цветом. """

    print("\033[31m {}" .format(text))


def out_green(text):
    """Выводит в консоль сообщение зеленым цветом. """

    print("\033[32m {}" .format(text))


def out_grey(text):
    """Выводит в консоль сообщение зеленым цветом. """

    print("\033[37m {}" .format(text))


def out_white(text):
    """Выводит в консоль сообщение зеленым цветом. """

    print("\033[38m {}" .format(text))
