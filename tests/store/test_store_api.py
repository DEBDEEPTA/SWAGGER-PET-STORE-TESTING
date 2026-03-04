import pytest

@pytest.mark.store
class TestStoreApi:

    def test_store_inventory(self,store_api):
        response = store_api.get_store_inventory()
        assert response.status_code == 200

    @pytest.mark.parametrize("id,pet_id,quantity",[(1,2,1),
                                                   (3,2,1),
                                                   (2,1,1),
                                                   (4,2,1)])
    def test_order_pet(self,store_api,order_factory,id,pet_id,quantity):
        my_order = order_factory(id=id,pet_id=pet_id,quantity=quantity)
        response = store_api.order_pet(my_order)

        assert response.status_code == 200
        assert response.json()['petId'] == pet_id

    @pytest.mark.parametrize("order_id",[1,3,4])
    def test_get_pet_by_order_id(self,order_id,store_api):
        response = store_api.get_by_order_id(order_id)

        assert response.status_code == 200

    @pytest.mark.parametrize("order_id",[3,2])
    def test_delete_order(self,store_api,order_id):
        response = store_api.delete_order(order_id)

        assert response.status_code == 200

