from selenium.webdriver.common.by import By


class ProfilePageLocators:

    # уникальный текст на странице
    PROFILE_PAGE_TEXT = (By.XPATH, "//p[contains(text(), 'В этом разделе вы можете')]")

    # ссылка "История заказов"
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")

    # кнопка "Выход"
    SIGNOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
