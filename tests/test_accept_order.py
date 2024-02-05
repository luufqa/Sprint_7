from unittest.mock import patch
import allure

from pages.accept_order import AcceptOrder


class TestAcceptOrder:
    @allure.title('Позитивный тест - возможно принять заказ')
    @patch('pages.accept_order.AcceptOrder.accept_order')
    def test_accept_order(self, mock_accept_order):
        accept_order = AcceptOrder()
        mock_accept_order.return_value = 200
        assert accept_order.accept_order() == 200
