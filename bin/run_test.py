"""Запускалка тестов. """

from trtr_mitya.core import get_tests, run


def main():
    """Точка входа. """

    # Получаем список тестов
    tests = get_tests()

    # Запускаем тесты по очереди
    run(*tests)


main()
