import allure
import requests
from pages.create_new_courier import CreateNewCourier
from pages.auth_courier import AuthUser
from pages.user_order import UserOrder

# Этот код работает, но раз через раз. Не нашел в чем проблема.
# Будто бы проблема в самом сервисе - баг может :/
# Только с этим методом проблема. test_accept_order.py замокировал.
class AcceptOrder:
    @allure.step('Принять заказ')
    def accept_order(self):
        auth_user = AuthUser()
        user_order = UserOrder()
        create_new_courier = CreateNewCourier()
        login_pass, response = create_new_courier.register_new_courier_and_return_login_password()
        courier_id = auth_user.auth_user(login_pass).json()
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/'
        params = {'courierId': courier_id['id']}
        order_id = user_order.user_order("BLACK").json()
        res = requests.put(f"{url}{order_id['track']}", params=params)
        return res.text