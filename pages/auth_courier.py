import allure
import requests
from data.data_pages import Args


class AuthCourier:
    @allure.step('Авторизация курьера')
    def auth_user(self, account):
        payload = {
            "login": account[0],
            "password": account[1]
        }
        response = requests.post(f'{Args.base_url}{Args.post_auth_courier}', data=payload)
        return response
