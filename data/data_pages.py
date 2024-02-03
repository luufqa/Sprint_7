class Args:
    # base_url
    base_url = 'https://qa-scooter.praktikum-services.ru'
    # accept_order.py
    put_accept_order = '/api/v1/orders/accept/'
    # auth_courier.py
    post_auth_courier = '/api/v1/courier/login'
    # create_courier.py
    post_create_new_courier = '/api/v1/courier'
    # delete_courier.py
    delete_courier = "/api/v1/courier/"
    # get_list_orders.py
    get_list_orders = '/api/v1/orders'
    # get_order_in_id.py
    get_order_in_id = '/api/v1/orders/track'
    # user_order.py
    post_user_order = '/api/v1/orders'


class Order:
    # применяются в user_order.py
    firstName = "aNaruto"
    lastName = "eUchiha"
    address = "Konoha, 142 apt."
    metroStation = 4
    phone = "+7 800 355 35 35"
    rentTime = 5
    deliveryDate = "2020-06-06"
    comment = "Saske, come back to Konoha"


class Fields:
    # применяются в test_create_courier.py
    empty_login = ["", "dasdasdas", '']
    empty_password = ["dasdasdas", "", 123]
    empty_login_and_password = ["", "", 'dasdasdas']
    error_data = 'Недостаточно данных для создания учетной записи'
