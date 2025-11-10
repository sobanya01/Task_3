from selenium.webdriver.common.by import By


class BasePageLocators:
    # таб "Конструктор"
    CONSTRUCTOR_TAB = (By.XPATH, "//header/nav//a//p[contains(text(), 'Конструктор')]")

    # таб "Лента Заказов"
    ORDER_FEED_TAB = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

    # ссылка "Личный Кабинет"
    PROFILE_LINK = (By.XPATH, "//header//a//p[contains(text(), 'Личный Кабинет')]")
