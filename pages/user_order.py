import allure
import requests
from data.data_pages import Args, Order



class UserOrder:
    @allure.step('Создание заказа')
    def user_order(self, color):
        data_order = {
            "firstName": Order.firstName,
            "lastName": Order.lastName,
            "address": Order.address,
            "metroStation": Order.metroStation,
            "phone": Order.phone,
            "rentTime": Order.rentTime,
            "deliveryDate": Order.deliveryDate,
            "comment": Order.comment,
            "color": [color]
        }
        response = requests.post(f'{Args.base_url}{Args.post_user_order}', json=data_order)
        return response
