import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from locators.main_page_locators import MainPageLocators


@allure.story("Основной функционал - Конструктор и Навигация")
class TestMainFunctionality:

    @allure.title("Проверка перехода по клику на 'Лента заказов'")
    def test_navigation_to_feed_from_constructor(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Открываем страницу Конструктора (главную)"):
            main_page.open_main_page()

        with allure.step("Кликаем на таб 'Лента Заказов'"):
            main_page.click_order_feed_tab()

        is_feed_page_opened = order_feed_page.is_feed_page_open()

        with allure.step("Проверяем, что открылась страница Ленты Заказов"):
            assert is_feed_page_opened, "Не открылась страница Ленты Заказов"

    @allure.title("Проверка перехода по клику на 'Конструктор'")
    def test_navigation_to_constructor_from_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Открываем страницу Ленты Заказов"):
            order_feed_page.open_feed_page()

        with allure.step("Кликаем на таб 'Конструктор'"):
            main_page.click_constructor_tab()

        is_constructor_page_opened = main_page.is_constructor_title_visible()

        with allure.step("Проверяем, что открылась страница Конструктора"):
            assert is_constructor_page_opened, "Не открылась страница Конструктора"

    @allure.title("Проверка открытия модального окна 'Детали ингредиента'")
    def test_ingredient_click_opens_details_modal(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()

        with allure.step("Кликаем на ингредиент (булку)"):
            main_page.click_ingredient()

        is_modal_opened = main_page.is_ingredient_modal_visible()

        with allure.step("Проверяем, что модальное окно 'Детали' открылось"):
            assert is_modal_opened, "Модальное окно 'Детали' не открылось"

    @allure.title("Проверка закрытия модального окна 'Детали ингредиента' по крестику")
    def test_ingredient_modal_closes_by_close_button(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную и кликаем на ингредиент"):
            main_page.open_main_page()
            main_page.click_ingredient()

        with allure.step("Закрываем модальное окно"):
            main_page.click_modal_close_button()

        is_not_visible_after_close = main_page.is_element_not_visible(MainPageLocators.MODAL_HEADER_TITLE)

        with allure.step("Проверяем, что модальное окно закрылось"):
            assert is_not_visible_after_close, "Модальное окно 'Детали ингредиента' не закрылось"

    @allure.title("Проверка увеличения счетчика при добавлении булки в заказ")
    def test_drag_ingredient_to_order_increases_counter(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()

        with allure.step("Перетаскиваем булку в конструктор"):
            main_page.drag_ingredient_to_order()

        bun_counter = main_page.get_bun_counter()

        with allure.step("Проверяем, что счетчик булки стал '2'"):
            assert bun_counter == "2", "Счетчик булки не равен 2"

    @allure.title("Проверка: авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_create_order(self, driver, user_data):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()

        with allure.step("Кликаем 'Войти в аккаунт'"):
            main_page.click_login_button_on_main()

        with allure.step("Логинимся, используя данные из фикстуры"):
            login_page.login(user_data["email"], user_data["password"])

        with allure.step("Добавляем булку в заказ"):
            main_page.drag_ingredient_to_order()

        with allure.step("Кликаем 'Оформить заказ'"):
            main_page.click_create_order_button()

        is_order_modal_shown = main_page.is_order_modal_visible()

        with allure.step("Проверяем, что появилось модальное окно 'Заказ оформлен'"):
            assert is_order_modal_shown, "Модальное окно 'Заказ оформлен' не появилось"
