import allure
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = Wait(driver, timeout)

    @allure.step("Получить адрес страницы")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Перейти на {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти {locator}")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти все элементы {locator}")
    def find_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить, что элемент {locator} НЕ виден на странице")
    def is_element_not_visible(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание, пока текст в {locator} не станет '{expected_text}'")
    def wait_for_text_to_be(self, locator, expected_text):
        try:
            self.wait.until(EC.text_to_be_present_in_element(locator, str(expected_text)))
            return True
        except TimeoutException:
            return False

    # методы для работы с хедером

    @allure.step("Клик по табу 'Конструктор' в хедере")
    def click_constructor_tab(self):
        self.click(BasePageLocators.CONSTRUCTOR_TAB)

    @allure.step("Клик по табу 'Лента Заказов' в хедере")
    def click_order_feed_tab(self):
        self.click(BasePageLocators.ORDER_FEED_TAB)

    @allure.step("Клик по ссылке 'Личный Кабинет' в хедере")
    def click_profile_link(self):
        self.click(BasePageLocators.PROFILE_LINK)
