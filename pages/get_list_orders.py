import allure
import requests

class GetListOrders:
    @allure.step('Получение списка заказов')
    def get_list_orders(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        return response