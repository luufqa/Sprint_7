import requests


class AuthUser:
    def auth_user(self, login_pass):
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        return response
