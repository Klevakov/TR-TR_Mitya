# TR-TR_Mitya представляет собой набор тестов для магазина [DNS](https://www.dns-shop.ru/) и был создан с целью изучить создание тестов на базе [Selenium](https://selenium.dev).

<p align="center">
    <img src="/logo/tr-tr-mitya.png" alt="TR-TR_Mitya">
</p>
</p>

## Установка
Клонируйте репозиторий командой: 
```bash
$ git clone git@github.com:Klevakov/TR-TR_Mitya.git
```

Установите сервер отображения браузера командами:

```bash
$ sudo apt update
$ sudo apt install xvfb
```

Установите Firefox браузер командой:

```bash
$ sudo apt install firefox-esr
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

## Запуск на хост-машине

Для запуска добавьте директорию проекта в переменную среды PYTHONPATH:

```bash
$ export PYTHONPATH="$PYTHONPATH:/TR-TR_Mitya/"
```

Запустите файл *run_test.py*

```bash
$ python3 bin/run_test.py
```

## Запуск тестов в Docker контейнере

Для создания образа контейнера в терминале перейдите в директорию проекта и введите команду:

```bash
$ docker build -t trtr-mitya -f DOCKER/Dockerfile .
```

Для запуска контейнера введите команду:
```bash
$ docker run -it --rm trtr-mitya
```