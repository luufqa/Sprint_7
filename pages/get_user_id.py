import allure
from pages.auth_courier import AuthCourier
from pages.create_courier import CreateCourier


class GetUserId:
    @allure.step('Получение ИД пользователя')
    def get_user_id(self):
        auth_user = AuthCourier()
        create_new_courier = CreateCourier()
        random_acc = create_new_courier.generate_courier_data()
        account, response = create_new_courier.create_courier(random_acc)
        return auth_user.auth_user(account)
