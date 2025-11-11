import allure
from pages.login_page import LoginPage
from pages.recover_password_page import RecoverPasswordPage
from urls import URL


@allure.story("Восстановление пароля")
class TestPasswordReset:

    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_forgot_password_link_redirects_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        recover_page = RecoverPasswordPage(driver)

        with allure.step("Открываем страницу логина"):
            login_page.open_login_page()

        with allure.step("Кликаем 'Восстановить пароль'"):
            login_page.click_recover_password_link()

        is_page_open = recover_page.is_recover_page_open()
        current_url = recover_page.current_url()

        with allure.step("Проверяем, что открылась страница восстановления пароля"):
            assert is_page_open, "Страница 'Восстановление пароля' не открылась"
            assert current_url == URL.PASSWORD_RESET_URL, "URL не соответствует странице восстановления"

    @allure.title("Проверка ввода email и клика по кнопке 'Восстановить'")
    def test_restore_button_click(self, driver):
        recover_page = RecoverPasswordPage(driver)

        with allure.step("Открываем страницу 'Восстановление пароля'"):
            recover_page.open_recover_password_page()

        with allure.step("Вводим email и кликаем 'Восстановить'"):
            recover_page.recover_password("test-email@yandex.ru")

    @allure.title("Проверка: клик по 'глазу' (на стр. Логина) делает поле 'Пароль' видимым")
    def test_password_visibility_toggle_makes_field_visible(self, driver):
        login_page = LoginPage(driver)

        with allure.step("Открываем страницу 'Логина'"):
            login_page.open_login_page()

        with allure.step("Вводим пароль"):
            login_page.set_password("123456")

        type_before = login_page.get_password_input_type()

        with allure.step("Кликаем на 'глаз'"):
            login_page.click_visibility_icon()

        type_after = login_page.get_password_input_type()

        with allure.step("Сравниваем типы поля 'до' и 'после' клика"):
            assert type_before == "password", "Изначально пароль не был скрыт (type != 'password')"
            assert type_after == "text", "Пароль не стал видимым (type != 'text')"
