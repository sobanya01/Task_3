import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from urls import URL


class ProfilePage(BasePage):

    @allure.step("Клик по ссылке 'История заказов'")
    def click_order_history_link(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Клик по кнопке 'Выход'")
    def click_signout_button(self):
        self.click(ProfilePageLocators.SIGNOUT_BUTTON)

    @allure.step("Проверка, что страница 'Личный кабинет' открыта")
    def is_profile_page_open(self):
        return self.is_element_visible(ProfilePageLocators.PROFILE_PAGE_TEXT)
