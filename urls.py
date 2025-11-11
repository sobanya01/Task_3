class URL:
    # базовый URL сайта
    MAIN_URL = "https://stellarburgers.education-services.ru"

    # базовый URL для API
    API_BASE_URL = f"{MAIN_URL}/api"

    # главная страница (Конструктор)
    MAIN_PAGE_URL = MAIN_URL

    # вход
    SIGNIN_URL = f"{MAIN_URL}/login"

    # восстановление пароля
    PASSWORD_RESET_URL = f"{MAIN_URL}/forgot-password"

    # лента заказов
    FEED_URL = f"{MAIN_URL}/feed"

    # история заказов (внутри личного кабинета)
    USER_ORDERS_HISTORY_URL = f"{MAIN_URL}/account/order-history"
