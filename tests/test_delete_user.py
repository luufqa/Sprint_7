import allure

from pages.get_user_id import GetUserId
from pages.delete_courier import DeleteCourier
import pytest


class TestDeleteUser:
    @allure.title('Тест удаления существующего пользователя')
    def test_delete_user_correct(self):
        delete_courier = DeleteCourier()
        get_user_id = GetUserId()
        user_id = get_user_id.get_user_id()
        result = delete_courier.delete_courier(user_id.json()['id'])
        assert result.json()['ok'] == True
        assert result.status_code == 200

    @allure.title('Тест удаления пользователя заменяя ИД на строковое значение')
    def test_delete_user_uncorrect(self):
        delete_courier = DeleteCourier()
        result = delete_courier.delete_courier("BLACK")
        assert result.status_code == 500
        assert 'invalid input syntax for type integer' in result.json()['message']

    @allure.title('Тест удаления пользователя заменяя ИД на нулевое значение')
    def test_delete_user_not_found(self):
        delete_courier = DeleteCourier()
        result = delete_courier.delete_courier(0)
        assert result.status_code == 404
        assert 'Курьера с таким id нет.' in result.json()['message']
