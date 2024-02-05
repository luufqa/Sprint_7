import allure
import requests
from data.data_pages import Args


class GetOrderInId:
    @allure.step('Получение заказа по номеру ИД')
    def get_order_in_id(self, order_id):
        params = {'t': order_id}
        res = requests.get(f"{Args.base_url}{Args.get_order_in_id}", params=params)
        return res
