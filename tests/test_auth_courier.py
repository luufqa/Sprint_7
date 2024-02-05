import allure
from pages.create_courier import CreateCourier
from pages.auth_courier import AuthCourier


class TestAuthUser:
    @allure.title('Позитивный тест - возможно авторизовать пользователя с корректными данными')
    def test_auth_user_correct(self):
        auth_user = AuthCourier()
        create_new_courier = CreateCourier()
        random_acc = create_new_courier.generate_courier_data()
        account, response = create_new_courier.create_courier(random_acc)
        result = auth_user.auth_user(account)
        assert result.json()['id'] is not None
        assert result.status_code == 200

    @allure.title('Негативный тест - невозможно авторизовать пользователя без логина')
    def test_auth_user_without_login(self):
        auth_user = AuthCourier()
        create_new_courier = CreateCourier()
        random_acc = create_new_courier.generate_courier_data()
        random_acc[0] = ''
        account, response = create_new_courier.create_courier(random_acc)
        result = auth_user.auth_user(account)
        assert "Недостаточно данных для входа" in result.json()['message']
        assert result.status_code == 400

    @allure.title('Негативный тест - невозможно авторизовать пользователя с несуществующим логином')
    def test_login_user_is_not_found(self):
        auth_user = AuthCourier()
        create_new_courier = CreateCourier()
        random_acc = create_new_courier.generate_courier_data()
        random_acc[0] = '112731237108371208372180371803710283718037180378017237128037'
        account, response = create_new_courier.create_courier(random_acc)
        result = auth_user.auth_user(account)
        assert "Учетная запись не найдена" in result.json()['message']
        assert result.status_code == 404
