import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.story("Лента заказов")
class TestOrderFeedPage:

    @allure.title("Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_feed_order_click_opens_details_modal(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Открываем страницу Ленты Заказов"):
            order_feed_page.open_feed_page()

        with allure.step("Кликаем по первому заказу в ленте"):
            order_feed_page.click_first_order_in_feed()

        with allure.step("Проверяем, что модальное окно открылось"):
            assert order_feed_page.is_order_details_modal_visible(), "Модальное окно 'Детали заказа' не открылось"

    @allure.title("Проверка: заказы пользователя отображаются в 'Ленте заказов'")
    def test_user_orders_from_history_appear_in_feed(self, driver, user_data):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.login_and_create_order(user_data["email"], user_data["password"])

        with allure.step("Получаем номер заказа (и модалка закрывается)"):
            order_number = main_page.get_order_number_and_close_modal()
            formatted_order_number = f"#{str(order_number).zfill(7)}"

        with allure.step("Переходим в Ленту Заказов"):
            order_feed_page.open_feed_page()

        with allure.step(f"Проверяем, что заказ {formatted_order_number} виден в ленте"):
            assert order_feed_page.wait_for_order_in_feed(
                formatted_order_number
            ), f"Заказ {formatted_order_number} не найден в общей ленте заказов"

    @allure.title("Проверка: при создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_new_order_increases_all_time_counter(self, driver, user_data):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        old_counter = order_feed_page.open_and_get_all_time_counter()

        main_page.login_and_create_order(user_data["email"], user_data["password"])

        with allure.step("Закрываем модальное окно 'Заказ оформлен'"):
            main_page.get_order_number_and_close_modal()

        with allure.step("Возвращаемся в Ленту Заказов и принудительно обновляем"):
            order_feed_page.open_feed_page()
            driver.refresh()  # <-- ИСПРАВЛЕНИЕ 1: Добавлено обновление

        expected_new_count = old_counter + 1
        with allure.step(f"Проверяем, что счетчик 'За всё время' увеличился до {expected_new_count}"):
            assert order_feed_page.wait_for_all_time_counter_to_be(
                expected_new_count
            ), f"Счетчик 'За всё время' не обновился до {expected_new_count}"

    @allure.title("Проверка: при создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_new_order_increases_today_counter(self, driver, user_data):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        old_counter = order_feed_page.open_and_get_today_counter()

        main_page.login_and_create_order(user_data["email"], user_data["password"])

        with allure.step("Закрываем модальное окно 'Заказ оформлен'"):
            main_page.get_order_number_and_close_modal()

        with allure.step("Возвращаемся в Ленту Заказов"):
            order_feed_page.open_feed_page()

        expected_new_count = old_counter + 1
        with allure.step(f"Проверяем, что счетчик 'За сегодня' увеличился до {expected_new_count}"):
            assert order_feed_page.wait_for_today_counter_to_be(
                expected_new_count
            ), f"Счетчик 'За сегодня' не обновился до {expected_new_count}"

    @allure.title("Проверка: после оформления заказа его номер появляется в разделе 'В работе'")
    def test_new_order_number_appears_in_progress_section(self, driver, user_data):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.login_and_create_order(user_data["email"], user_data["password"])

        with allure.step("Получаем номер заказа (и модалка закрывается)"):
            order_number = main_page.get_order_number_and_close_modal()
            order_number_formatted = str(order_number).zfill(7)

        with allure.step("Переходим в Ленту Заказов"):
            order_feed_page.open_feed_page()

        with allure.step(f"Проверяем, что заказ {order_number_formatted} появился 'В работе'"):
            assert order_feed_page.wait_for_order_in_progress(
                order_number_formatted
            ), f"Заказ {order_number_formatted} не найден в секции 'В работе'"
