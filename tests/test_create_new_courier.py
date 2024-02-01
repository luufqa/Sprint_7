import allure
from pages.delete_courier import DeleteCourier
from pages.auth_courier import AuthUser
from pages.create_new_courier import CreateNewCourier
import unittest


class TestNewCourier(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        auth_user = AuthUser()
        delete_courier = DeleteCourier()
        res = auth_user.auth_user(self.login_pass)
        print(res.text)
        delete_courier.delete_courier(res.json()['id'])
    @allure.title('Тест создания новый уч.записи курьера с корректными данными')
    def test_create_new_courier_correct(self):
        create_new_courier = CreateNewCourier()
        self.login_pass, response = create_new_courier.register_new_courier_and_return_login_password()
        print(self.login_pass)
        assert response.text == '{"ok":true}'
        assert response.status_code == 201


    @allure.title('Тест создания идентичной уч.записи (дубляж)')
    def test_create_identic_courier(self):
        user = CreateNewCourier()
        self.login_pass, response = user.register_new_courier_and_return_login_password()
        identic_user = user.register_identic_new_courier(self.login_pass)
        assert identic_user.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
        assert identic_user.status_code == 409


class TestNewCourierWithoutLogin:
    @allure.title('Тест создания новой уч.записи курьера без логина')
    def test_create_new_courier_without_login(self):
        user = CreateNewCourier()
        self.login_pass, response = user.register_new_courier_and_return_login_password()
        self.login_pass[0] = ' '
        result = user.register_identic_new_courier(self.login_pass)
        assert "Этот логин уже используется. Попробуйте другой." in result.json()['message']
        assert result.status_code == 409





