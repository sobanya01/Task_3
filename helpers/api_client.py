import requests
from helpers.helpers import generate_random_string
from urls import URL


class ApiClient:
    # генерирует случайные email, password и name.
    def generate_random_user(self):
        email = f"{generate_random_string(10)}@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)

        return {"email": email, "password": password, "name": name}

    # создает пользователя через API.
    def create_user(self):
        user_data = self.generate_random_user()

        response = requests.post(f"{URL.API_BASE_URL}/auth/register", json=user_data)
        token = response.json()["accessToken"]

        return user_data, token

    # удаляет пользователя по токену.
    def delete_user(self, token):
        headers = {"Authorization": token}

        requests.delete(f"{URL.API_BASE_URL}/auth/user", headers=headers)
