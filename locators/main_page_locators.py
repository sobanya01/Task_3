from selenium.webdriver.common.by import By


class MainPageLocators:
    # фон, который перекрывает клики
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

    # заголовок "Соберите бургер"
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    # кнопка "Войти в аккаунт" (для неавторизованного пользователя)
    MAIN_PAGE_SIGNIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # кнопка "Оформить заказ" (для авторизованного пользователя)
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # область для перетаскивания (корзина)
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    # ингредиенты
    BUN_FLUORESCENT_ITEM = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    BUN_FLUORESCENT_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a/div/p")

    # модальное окно "Детали ингредиента"
    MODAL_HEADER_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_INGR_CLOSE_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'modal__container')]//button[contains(@class,'modal__close')]",
    )

    # модальное окно "Заказ оформлен"
    MODAL_ORDER_CONFIRM_TITLE = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    MODAL_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    MODAL_ORDER_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close_modified')]",
    )
    MODAL_OVERLAY_GIF = (By.XPATH, "//img[contains(@alt, 'loading animation')]")
