import allure

from pages.create_new_courier import CreateNewCourier
from pages.auth_courier import AuthUser


class TestAuthUser:
    @allure.title('Тест авторизации пользователя с корректными данными')
    def test_auth_user_correct(self):
        auth_user = AuthUser()
        create_new_courier = CreateNewCourier()
        login_pass, response = create_new_courier.register_new_courier_and_return_login_password()
        result = auth_user.auth_user(login_pass)
        assert result.json()['id'] is not None
        assert result.status_code == 200

    @allure.title('Тест авторизации пользователя без логина')
    def test_auth_user_without_login(self):
        auth_user = AuthUser()
        create_new_courier = CreateNewCourier()
        login_pass, response = create_new_courier.register_new_courier_and_return_login_password()
        login_pass[0] = ''
        result = auth_user.auth_user(login_pass)
        assert "Недостаточно данных для входа" in result.json()['message']
        assert result.status_code == 400

    @allure.title('Тест авторизации пользователя с несуществующим логином')
    def test_login_user_is_not_found(self):
        auth_user = AuthUser()
        create_new_courier = CreateNewCourier()
        login_pass, response = create_new_courier.register_new_courier_and_return_login_password()
        login_pass[0] = '112731237108371208372180371803710283718037180378017237128037'
        result = auth_user.auth_user(login_pass)
        assert "Учетная запись не найдена" in result.json()['message']
        assert result.status_code == 404