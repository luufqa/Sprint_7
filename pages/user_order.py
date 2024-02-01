import allure
import requests


class UserOrder:
    @allure.step('Создание заказа')
    def user_order(self, color):
        data_order = {
            "firstName": "aNaruto",
            "lastName": "eUchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=data_order)
        return response
