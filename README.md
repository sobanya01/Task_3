# Task 3: UI-тесты Stellar Burgers

Автоматизированные UI‑тесты для веб‑приложения Stellar Burgers на `pytest + selenium` с отчётами `Allure`. Поддерживаются браузеры: Google Chrome (по умолчанию) и Mozilla Firefox.


## Структура проекта

- `tests/` — тестовые сценарии:
  - `test_main_functionality.py` — базовые проверки главной страницы и конструктора
  - `test_order_feed.py` — лента заказов
  - `test_password_reset.py` — восстановление/сброс пароля
  - `test_user_profile.py` — личный кабинет и профиль
- `pages/` — Page Object'ы (логика страниц):
  - `base_page.py`, `main_page.py`, `login_page.py`, `profile_page.py`, `order_feed_page.py`, `recover_password_page.py`, `reset_password_page.py`
- `locators/` — локаторы элементов страниц
- `helpers/` — вспомогательный код:
  - `helpers.py` — фабрика вебдрайверов (`WebdriverFactory`), генератор строк
  - `api_client.py` — клиент для API (создание/удаление тестового пользователя)
- `conftest.py` — фикстуры `pytest`:
  - `driver` — инициализация/закрытие браузера (опция `--browser_name=chrome|firefox`)
  - `user_data` — создание и удаление тестового пользователя через API
- `urls.py` — все используемые URL приложения и API
- `requirements.txt` — зависимости проекта
- `allure_results/` — папка с сырыми результатами Allure (создаётся при запуске с `--alluredir`)


## Требования

- Python 3.10+
- Google Chrome и/или Mozilla Firefox
- Рекомендуется установить Allure CLI для просмотра отчётов:
  - macOS: `brew install allure`
  - Windows: через Scoop/Chocolatey или с сайта `https://docs.qameta.io/allure/`


## Установка

1) Клонируйте репозиторий и перейдите в папку проекта

2) Создайте и активируйте виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
# .venv\Scripts\activate     # Windows PowerShell
```

3) Установите зависимости

```bash
pip install -r requirements.txt
```


## Запуск тестов

- По умолчанию (Chrome):

```bash
pytest -v
```

- Явный выбор браузера:

```bash
pytest -v --browser_name=chrome
pytest -v --browser_name=firefox
```

- Запуск конкретного файла/теста:

```bash
pytest -v tests/test_order_feed.py
pytest -v tests/test_user_profile.py::TestUserProfile::test_profile_to_order_history_navigation
```


## Allure-отчёты

1) Сгенерировать результаты при прогоне:

```bash
pytest -v --alluredir=allure_results
```

2) Открыть отчёт (Allure CLI должен быть установлен):

```bash
allure serve allure_results
```

Либо сгенерировать статический отчёт:

```bash
allure generate allure_results -o allure-report --clean
```


## Полезно знать

- Временные тестовые пользователи создаются/удаляются автоматически фикстурой `user_data` через API (`helpers/api_client.py`).
- Драйверы Chrome/Firefox подгружаются автоматически через `webdriver-manager` при первом запуске.
- Базовый URL и все маршруты собраны в `urls.py`. При необходимости поменяйте `URL.MAIN_URL` для перенастройки среды.


## Частые проблемы

- `allure: command not found` — установите Allure CLI (см. раздел Требования) и перезапустите терминал.
- Браузер не открывается/закрывается — убедитесь, что установлен совместимый Chrome/Firefox и есть права на установку драйверов.
- Конфликт версий Python/зависимостей — пересоздайте виртуальное окружение и переустановите зависимости.
