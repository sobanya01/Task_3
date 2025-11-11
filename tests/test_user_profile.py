import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from urls import URL


@allure.story("Личный кабинет / Профиль пользователя")
class TestUserProfile:

    @allure.title("Проверка перехода в 'Личный кабинет' по клику на хедер")
    def test_personal_account_link_click_opens_profile_page(self, driver, user_data):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Логинимся"):
            main_page.open_main_page()
            main_page.click_login_button_on_main()
            login_page.login(user_data["email"], user_data["password"])
            main_page.is_constructor_title_visible()

        with allure.step("Кликаем на 'Личный Кабинет' в хедере"):
            main_page.click_profile_link()

        is_profile_open = profile_page.is_profile_page_open()

        with allure.step("Проверяем, что открылась страница Профиля"):
            assert is_profile_open, "Страница Профиля не открылась"

    @allure.title("Проверка перехода в раздел 'История заказов' из личного кабинета")
    def test_profile_to_order_history_navigation(self, driver, user_data):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Логинимся и переходим в 'Личный кабинет'"):
            main_page.open_main_page()
            main_page.click_login_button_on_main()
            login_page.login(user_data["email"], user_data["password"])
            main_page.is_constructor_title_visible()
            main_page.click_profile_link()

        with allure.step("Кликаем на 'История заказов'"):
            profile_page.click_order_history_link()

        actual_url = profile_page.current_url()

        with allure.step("Проверяем, что URL изменился на 'Историю заказов'"):
            assert actual_url == URL.USER_ORDERS_HISTORY_URL, "Неверный URL"

    @allure.title("Проверка выхода из аккаунта")
    def test_logout_from_personal_account(self, driver, user_data):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Логинимся и переходим в 'Личный кабинет'"):
            main_page.open_main_page()
            main_page.click_login_button_on_main()
            login_page.login(user_data["email"], user_data["password"])
            main_page.is_constructor_title_visible()
            main_page.click_profile_link()

        with allure.step("Кликаем на 'Выход'"):
            profile_page.click_signout_button()

        is_login_page_open = login_page.is_login_page_open()

        with allure.step("Проверяем, что открылась страница Логина"):
            assert is_login_page_open, "Не произошел выход из аккаунта (не открылась страница Логина)"
