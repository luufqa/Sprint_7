import allure
from pages.get_order_in_id import GetOrderInId
from pages.user_order import UserOrder


class TestGetOrderInId:
    @allure.title('Позитивный тест - возможно получить заказ по корректному ИД')
    def test_get_order_in_id_correct(self):
        get_some_methods = GetOrderInId()
        user_order = UserOrder()
        order_id = user_order.user_order("BLACK")
        result = get_some_methods.get_order_in_id(order_id.json()['track'])
        assert result.status_code == 200
        assert result.json()['order'] is not None


    @allure.title('Негативый тест - невозможно получить заказ по несуществующему ИД')
    def test_get_order_in_id_not_found(self):
        get_some_methods = GetOrderInId()
        result = get_some_methods.get_order_in_id('0000009')
        assert result.status_code == 404
        assert 'Заказ не найден' in result.json()['message']

    @allure.title('Негативный тест - невозможно получить заказ, когда длинное значению ИД')
    def test_get_order_in_id_out_of_range(self):
        get_some_methods = GetOrderInId()
        result = get_some_methods.get_order_in_id("1414141341341241241234141414144134")
        assert result.status_code == 500
        assert 'out of range for type integer' in result.json()['message']
