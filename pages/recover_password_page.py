import allure
from pages.base_page import BasePage
from locators.recover_password_page_locators import RecoverPasswordPageLocators
from urls import URL


class RecoverPasswordPage(BasePage):

    @allure.step("Открытие страницы 'Восстановление пароля'")
    def open_recover_password_page(self):
        self.open(URL.PASSWORD_RESET_URL)

    @allure.step("Ввод email: {email}")
    def set_email(self, email):
        self.find(RecoverPasswordPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_recover_button(self):
        self.click(RecoverPasswordPageLocators.RECOVER_BUTTON)

    @allure.step("Выполнение восстановления пароля для email: {email}")
    def recover_password(self, email):
        self.set_email(email)
        self.click_recover_button()

    @allure.step("Проверка, что страница 'Восстановление пароля' открыта")
    def is_recover_page_open(self):
        return self.is_element_visible(RecoverPasswordPageLocators.RECOVER_FORM_TITLE)
