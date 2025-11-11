import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import URL


class MainPage(BasePage):
    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.open(URL.MAIN_PAGE_URL)

    @allure.step("Клик по кнопке 'Войти в аккаунт' на главной")
    def click_login_button_on_main(self):
        self.click(MainPageLocators.MAIN_PAGE_SIGNIN_BUTTON)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_create_order_button(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Клик по ингредиенту (булке)")
    def click_ingredient(self):
        self.click(MainPageLocators.BUN_FLUORESCENT_ITEM)

    @allure.step("Закрытие модального окна 'Детали ингредиента'")
    def click_modal_close_button(self):
        self.click(MainPageLocators.MODAL_INGR_CLOSE_BUTTON)

    @allure.step("Перетаскивание ингредиента (булки) в конструктор")
    def drag_ingredient_to_order(self):
        source = self.find(MainPageLocators.BUN_FLUORESCENT_ITEM)
        target = self.find(MainPageLocators.CONSTRUCTOR_DROP_AREA)

        js_code = """
        const dataTransfer = new DataTransfer();
        ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'].forEach(eventType => {
            const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
            (eventType === 'dragstart' || eventType === 'dragend' ? arguments[0] : arguments[1]).dispatchEvent(event);
        });
        """

        self.execute_script(js_code, source, target)

    @allure.step("Проверка, что главная страница открыта")
    def is_constructor_title_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Проверка, что модальное окно 'Детали ингредиента' открыто")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.MODAL_HEADER_TITLE)

    @allure.step("Проверка, что модальное окно 'Детали ингредиента' закрыто")
    def is_ingredient_modal_closed(self):
        return self.is_element_not_visible(MainPageLocators.MODAL_HEADER_TITLE)

    @allure.step("Проверка, что модальное окно 'Заказ оформлен' открыто")
    def is_order_modal_visible(self):
        return self.is_element_visible(MainPageLocators.MODAL_ORDER_CONFIRM_TITLE)

    @allure.step("Получение счетчика ингредиента (булки)")
    def get_bun_counter(self):
        return self.find(MainPageLocators.BUN_FLUORESCENT_COUNTER).text

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number_from_modal(self):
        order_number_element = self.find(MainPageLocators.MODAL_ORDER_NUMBER)
        return order_number_element.text

    @allure.step("Получение номера заказа и закрытие модального окна")
    def get_order_number_and_close_modal(self):
        self.is_element_not_visible(MainPageLocators.MODAL_OVERLAY_GIF)
        order_number = self.get_order_number_from_modal()

        self.click(MainPageLocators.MODAL_ORDER_CLOSE_BUTTON)

        self.is_element_not_visible(MainPageLocators.MODAL_ORDER_CONFIRM_TITLE)
        return order_number
