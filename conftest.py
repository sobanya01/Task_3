import pytest
from helpers.helpers import WebdriverFactory
from helpers.api_client import ApiClient


# чтобы запускать тесты так: pytest --browser_name=chrome
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Выберите браузер: chrome или firefox",
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver = WebdriverFactory.create_browser(browser_name)

    yield driver

    driver.quit()


# создание и удаление пользователя
@pytest.fixture
def user_data():
    api = ApiClient()
    data, token = api.create_user()

    user_info = {"email": data["email"], "password": data["password"], "token": token}

    yield user_info

    api.delete_user(token)
