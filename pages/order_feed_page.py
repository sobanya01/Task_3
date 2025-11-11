import allure
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from urls import URL


class OrderFeedPage(BasePage):

    @allure.step("Открытие страницы 'Лента заказов'")
    def open_feed_page(self):
        self.open(URL.FEED_URL)

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order_in_feed(self):
        self.click(OrderFeedPageLocators.FIRST_ORDER_IN_FEED)

    @allure.step("Проверка, что страница 'Лента заказов' открыта")
    def is_feed_page_open(self):
        return self.is_element_visible(OrderFeedPageLocators.FEED_PAGE_TITLE)

    @allure.step("Проверка, что модальное окно 'Детали заказа' открыто")
    def is_order_details_modal_visible(self):
        return self.is_element_visible(OrderFeedPageLocators.MODAL_ORDER_DETAILS_TITLE)

    @allure.step("Получение значения счетчика 'Выполнено за всё время'")
    def get_all_time_counter(self):
        counter_str = self.find(OrderFeedPageLocators.ALL_TIME_COUNTER).text
        return int(counter_str)

    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def get_today_counter(self):
        counter_str = self.find(OrderFeedPageLocators.TODAY_COUNTER).text
        return int(counter_str)

    @allure.step("Ожидание, пока счетчик 'За сегодня' не станет {expected_count}")
    def wait_for_today_counter_to_be(self, expected_count):
        try:
            self.wait.until(lambda driver: self.get_today_counter() == expected_count)
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание, пока счетчик 'За всё время' не станет {expected_count}")
    def wait_for_all_time_counter_to_be(self, expected_count):
        try:
            self.wait.until(lambda driver: self.get_all_time_counter() == expected_count)
            return True
        except TimeoutException:
            return False

    @allure.step("Открыть страницу ленты и получить счетчик 'За всё время'")
    def open_and_get_all_time_counter(self):
        self.open_feed_page()
        return self.get_all_time_counter()

    @allure.step("Открыть страницу ленты и получить счетчик 'За сегодня'")
    def open_and_get_today_counter(self):
        self.open_feed_page()
        return self.get_today_counter()

    @allure.step("Получение списка номеров заказов 'В работе'")
    def get_in_progress_order_numbers(self):
        order_elements = self.find_elements(OrderFeedPageLocators.IN_PROGRESS_ALL_ORDERS)
        return [element.text for element in order_elements]

    @allure.step("Ожидание появления заказа {order_number} в списке 'В работе'")
    def wait_for_order_in_progress(self, order_number):
        try:
            self.wait.until(lambda driver: order_number in self.get_in_progress_order_numbers())
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание появления заказа {order_number} в ленте")
    def wait_for_order_in_feed(self, order_number):

        order_locator = OrderFeedPageLocators.get_order_by_number_locator(order_number)

        return self.is_element_visible(order_locator)
