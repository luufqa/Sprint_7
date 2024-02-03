import allure
import requests
import random
import string
from data.data_pages import Args


class CreateCourier:

    @allure.step('Генерация строкового значения')
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Генерация данных для аккаунта')
    def generate_courier_data(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)
        return [login, password, first_name]

    @allure.step('Создание курьера. Возврат аккаунта и ответа')
    def create_courier(self, account):
        payload = {
            "login": account[0],
            "password": account[1],
            "firstName": account[2]
        }
        response = requests.post(f'{Args.base_url}{Args.post_create_new_courier}', data=payload)
        return account, response
