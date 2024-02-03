import allure
import requests
from data.data_pages import Args

class GetListOrders:
    @allure.step('Получение списка заказов')
    def get_list_orders(self):
        response = requests.get(f'{Args.base_url}{Args.get_list_orders}')
        return response