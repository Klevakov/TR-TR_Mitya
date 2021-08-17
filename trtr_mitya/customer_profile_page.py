"""Тесты личного кабинета в ИМ DNS. """

from conf.settings import EMAIL, PASSWORD
from .core import TestBase


class CustomerProfilePageTest(TestBase):
    """Набор тестов для личного кабинета покупателя в ИМ DNS. """

    def test_sign_in(self):
        """Тест входа в личный кабинет. """

        # Нажимаем на "Вход"
        self.check_and_click('.header__login_button')

        # Проверяем, что мы попали на всплывающее окно входа в ЛК
        self.wait_for_visible_element('.form-entry-or-registry')
        assert self.check_by_css('.form-entry-or-registry')

        # Кликаем на ссылку "Войти в паролем"
        self.check_and_click('.block-other-login-methods__password-caption')

        # Вводим логин и пароль
        self.wait_for_visible_element('input[autocomplete="username"]').send_keys(EMAIL)
        self.wait_for_visible_element('input[autocomplete="current-password"]').send_keys(PASSWORD)

        # Нажимаем на кнопку "Войти"
        self.check_and_click('.base-ui-button')

        # Проверяем, что зашли в личный кабинет
        self.wait_for_visible_element('.header-profile__level_pie')
        assert self.check_by_css('.header-profile__level_pie')
