import allure
import requests
from data.data_pages import Args


class DeleteCourier:
    @allure.step('Удаление курьера')
    def delete_courier(self, user_id):
        response = requests.delete(f"{Args.base_url}{Args.delete_courier}{user_id}")
        return response
