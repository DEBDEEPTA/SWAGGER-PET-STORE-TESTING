import pytest
from src.store_api import StoreApi
from src.models.order import Order
@pytest.fixture
def store_api():
    return StoreApi()


@pytest.fixture
def order_factory():
    def create_factory(id,pet_id,quantity):
        my_order = Order(
            id = id,
            petId= pet_id,
            quantity= quantity
        )
        return my_order
    return create_factory