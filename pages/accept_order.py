import requests

class AccepterOrder:
    def accept_order(self):
        user = User()
        login_pass, response = user.register_new_courier_and_return_login_password()
        courier_id = user.auth_user(login_pass).json()
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/'
        params = {'courierId': courier_id['id']}
        order_id = user.order_user("BLACK").json()
        res = requests.put(f"{url}{order_id['track']}", params=params)
        return res.text