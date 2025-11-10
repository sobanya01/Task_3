import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import URL


class LoginPage(BasePage):

    @allure.step("Открытие страницы входа")
    def open_login_page(self):
        self.open(URL.SIGNIN_URL)

    @allure.step("Ввод email: {email}")
    def set_email(self, email):
        self.find(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step("Ввод пароля")
    def set_password(self, password):
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_FORM_BUTTON)

    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_recover_password_link(self):
        self.click(LoginPageLocators.RECOVER_PASSWORD_LINK)

    @allure.step("Выполнение входа пользователя с email: {email}")
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    @allure.step("Проверка, что страница входа открыта (виден заголовок 'Вход')")
    def is_login_page_open(self):
        return self.is_element_visible(LoginPageLocators.LOGIN_FORM_TITLE)

    @allure.step("Клик по иконке 'показать/скрыть пароль'")
    def click_visibility_icon(self):
        self.click(LoginPageLocators.PASSWORD_VISIBILITY_ICON)

    @allure.step("Получение типа поля 'Пароль' (password или text)")
    def get_password_input_type(self):
        return self.find(LoginPageLocators.PASSWORD_INPUT).get_attribute("type")
