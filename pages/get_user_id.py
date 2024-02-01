import allure

from pages.auth_courier import AuthUser
from pages.create_new_courier import CreateNewCourier


class GetUserId:
    @allure.step('Получение ИД курьера')
    def get_user_id(self):
        auth_user = AuthUser()
        create_new_courier = CreateNewCourier()
        login_pass, response = create_new_courier.register_new_courier_and_return_login_password()
        return auth_user.auth_user(login_pass)
