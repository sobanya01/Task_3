from selenium.webdriver.common.by import By


class LoginPageLocators:

    # Иконка "показать/скрыть пароль"
    PASSWORD_VISIBILITY_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]")

    # заголовок "Вход"
    LOGIN_FORM_TITLE = (By.XPATH, "//h2[text()='Вход']")

    # поле "Email"
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    # кнопка "Войти"
    LOGIN_FORM_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # ссылка "Восстановить пароль"
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
