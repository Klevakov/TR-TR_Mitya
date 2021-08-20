TR-TR_Mitya представляет собой набор тестов для магазина [DNS](https://www.dns-shop.ru/) и был создан с целью изучить создание тестов на базе [Selenium](https://selenium.dev).
<p align="center">
    <img src="/logo/tr-tr-mitya.png" alt="TR-TR_Mitya">
</p>

## Установка
Клонируйте репозиторий командой: 
```bash
$ git clone git@github.com:Klevakov/TR-TR_Mitya.git
```

Создайте и активируйте виртуальное окружение.

```bash
$ python3 -m venv env
$ source env/bin/activate
```

Установите зависимости проекта в его виртуальное окружение командой:

```bash
$ pip install -r requirements.txt
```

## Запуск

Для запуска добавьте директорию проекта в переменную среды PYTHONPATH:

```bash
$ export PYTHONPATH="$PYTHONPATH:/TR-TR_Mitya/"
```

Запустите файл *run_test.py*

```bash
$ python3 bin/run_test.py
```

