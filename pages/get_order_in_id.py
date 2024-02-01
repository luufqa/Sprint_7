import allure
import requests


class GetOrderInId:
    @allure.step('Получение заказа по номеру ИД')
    def get_order_in_id(self, order_id):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/track'
        params = {'t': order_id}
        res = requests.get(f"{url}", params=params)
        return res
