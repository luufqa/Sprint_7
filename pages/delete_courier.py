import allure
import requests


class DeleteCourier:
    @allure.step('Удаление курьера')
    def delete_courier(self, user_id):
        response = requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{user_id}")
        return response
