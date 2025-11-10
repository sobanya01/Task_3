from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    # заголовок
    FEED_PAGE_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

    # первый заказ в ленте
    FIRST_ORDER_IN_FEED = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]")

    # модальное окно "Детали заказа"
    MODAL_ORDER_DETAILS_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'Modal_orderBox') and contains(@class, 'Modal_modal__contentBox')]",
    )

    # "закрыть" в модальном окне "Детали заказа"
    MODAL_ORDER_CLOSE_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'modal__container')]//button[contains(@class,'modal__close')]",
    )

    # счетчик "Выполнено за всё время"
    ALL_TIME_COUNTER = (By.XPATH, "//p[normalize-space(text())='Выполнено за все время:']/following-sibling::p")

    # счетчик "Выполнено за сегодня"
    TODAY_COUNTER = (By.XPATH, "//p[normalize-space(text())='Выполнено за сегодня:']/following-sibling::p")

    # все номера заказов в ленте
    ALL_ORDER_NUMBERS_IN_FEED = (
        By.XPATH,
        "//a[contains(@class, 'OrderHistory_link')]//p[contains(@class, 'text_type_digits-default')]",
    )

    # все номера заказов "В работе"
    IN_PROGRESS_ALL_ORDERS = (
        By.XPATH,
        "//p[normalize-space(text())='В работе:']/following-sibling::ul/li",
    )
