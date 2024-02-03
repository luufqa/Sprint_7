import allure
from pages.get_list_orders import GetListOrders


class TestGetListOrders:
    @allure.title('Позитивный тест - возможно получить список заказов')
    def test_get_list_orders(self):
        get_some_methods = GetListOrders()
        result = get_some_methods.get_list_orders()
        assert result.json()['orders'] is not None
        assert result.status_code == 200
