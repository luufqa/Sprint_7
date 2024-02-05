import allure
from pages.create_courier import CreateCourier
import pytest
from data.data_pages import Fields


class TestNewCourier():
    @allure.title('Позитивный тест - возможно создать аккаунт курьера с корректными данными')
    def test_create_courier_correct(self):
        create_new_courier = CreateCourier()
        random_acc = create_new_courier.generate_courier_data()
        self.account, response = create_new_courier.create_courier(random_acc)
        assert response.text == '{"ok":true}'
        assert response.status_code == 201

    @allure.title('Негативный тест - невозможно создать идентичный аккаунт (дубляж)')
    def test_create_courier_identic(self):
        create_new_courier = CreateCourier()
        random_acc = create_new_courier.generate_courier_data()
        account, response = create_new_courier.create_courier(random_acc)
        identic_register, response = create_new_courier.create_courier(account)
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
        assert response.status_code == 409

    @allure.title(
        'Негативный тест - невозможно создать аккаунт, не заполнив обязательные поля. Обязательными полями считаются Login и Password')
    @pytest.mark.parametrize("account_data, expected",
                             [(Fields.empty_login, Fields.error_data),
                              (Fields.empty_password, Fields.error_data),
                              (Fields.empty_login_and_password, Fields.error_data)])
    def test_create_courier_uncorrect(self, account_data, expected):
        create_new_courier = CreateCourier()
        account, response = create_new_courier.create_courier(account_data)
        assert response.json()['message'] == expected
        assert response.status_code == 400
