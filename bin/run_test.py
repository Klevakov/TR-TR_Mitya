#!/usr/bin/env python3
"""Запускалка тестов. """

from trtr_mitya.core import get_tests, run


def main():
    """Точка входа. """

    # Получаем список тестов
    tests = get_tests()

    # Запускаем тесты по очереди
    run(*tests)


if __name__ == '__main__':
    main()
