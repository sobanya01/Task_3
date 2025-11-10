class URL:
    # базовый URL сайта
    MAIN_URL = "https://stellarburgers.education-services.ru"

    # базовый URL для API
    API_BASE_URL = f"{MAIN_URL}/api"

    # главная страница (Конструктор)
    MAIN_PAGE_URL = MAIN_URL

    # регистрация
    SIGNUP_URL = f"{MAIN_URL}/register"

    # вход
    SIGNIN_URL = f"{MAIN_URL}/login"

    # восстановление пароля
    PASSWORD_RESET_URL = f"{MAIN_URL}/forgot-password"

    # сброс пароля (страница, куда попадаешь после восстановления)
    PASSWORD_SET_NEW_URL = f"{MAIN_URL}/reset-password"

    # лента заказов
    FEED_URL = f"{MAIN_URL}/feed"

    # личный кабинет (профиль)
    USER_PROFILE_URL = f"{MAIN_URL}/profile"

    # история заказов (внутри личного кабинета)
    USER_ORDERS_HISTORY_URL = f"{USER_PROFILE_URL}/orders"
