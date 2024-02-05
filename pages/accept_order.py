import allure
import requests
from pages.create_courier import CreateCourier
from pages.auth_courier import AuthCourier
from pages.user_order import UserOrder
from data.data_pages import Args


# На тестируемом ресурсе явный баг
# в методе accept_order код работает, но раз через раз
class AcceptOrder:
    @allure.step('Принять заказ')
    def accept_order(self):
        auth_user = AuthCourier()
        user_order = UserOrder()
        create_new_courier = CreateCourier()
        random_acc = create_new_courier.generate_courier_data()
        account, response = create_new_courier.create_courier(random_acc)
        courier_id = auth_user.auth_user(account).json()
        order_id = user_order.user_order("BLACK").json()
        params = {'courierId': courier_id['id']}
        res = requests.put(f"{Args.base_url}{Args.put_accept_order}{order_id['track']}", params=params)
        return res.text