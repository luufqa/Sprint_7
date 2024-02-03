import allure
from pages.user_order import UserOrder
import pytest


class TestNewOrder:

    @allure.title('Позитивный тест - возможно создать заказ, применяя допустимые значения Color')
    @pytest.mark.parametrize("color, expected", [("BLACK", 201), ("GREY", 201), ("", 201)])
    def test_create_order(self, color, expected):
        user_order = UserOrder()
        result = user_order.user_order(color)
        assert result.status_code == expected
        assert result.json()['track'] is not None
