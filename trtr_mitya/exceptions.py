"""Модуль, содержащий исключения для TR-TR-Mitya. """


class InvalidElementValue(Exception):
    """
    Исключение возникает, когда элемент найден,
    но его значение не соответствует ожидаемому.
    """

    def __init__(self, text='Элемент найден, но его значение не соответствует ожидаемому'):
        self.txt = text

    def __str__(self):
        return self.txt
