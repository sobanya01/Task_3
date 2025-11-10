from selenium.webdriver.common.by import By


class RecoverPasswordPageLocators:

    # заголовок
    RECOVER_FORM_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")

    # поле "Email"
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # кнопка "Восстановить"
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
