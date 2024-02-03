import pytest
from pages.auth_courier import AuthCourier
from pages.delete_courier import DeleteCourier

@pytest.fixture(autouse=True)
def fixture(request):
    account = getattr(request.node.cls, 'account', None)
    yield
    # Фикстура, которая применяется только к test_create_new_courier_correct
    # в тестовом модуле test_create_new_courier.py
    if request.node.name == "test_create_new_courier_correct":
        auth_user = AuthCourier()
        if account is not None:
            res = auth_user.auth_user(account)
            delete_courier = DeleteCourier()
            delete_courier.delete_courier(res.json()['id'])
    else:
        pass