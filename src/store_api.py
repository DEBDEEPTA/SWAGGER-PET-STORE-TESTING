from utils.api_client import ApiClient
from src.models.order import Order
from dataclasses import  asdict
import json
class StoreApi:
    def __init__(self):
        self.client = ApiClient("https://petstore.swagger.io/v2")

    def get_store_inventory(self):
       return self.client.get(endpoint="/store/inventory")

    def order_pet(self, order:Order):
        payload = asdict(order)
        return self.client.post(endpoint="/store/order", json = payload)


    def get_by_order_id(self,order_id:int):
        endpoint = f"/store/order/{order_id}"
        return self.client.get(endpoint=endpoint)

    def delete_order(self,order_id:int):
        endpoint = f"/store/order/{order_id}"
        return self.client.delete(endpoint=endpoint)


if __name__=="__main__":
    store_api = StoreApi()

    # GET STORE INVENTORY STATUS
    print("=" * 20 + "PET STORE INVENTORY" + "=" * 20)
    response_store_inv = store_api.get_store_inventory()
    print(json.dumps(response_store_inv.json(), indent=4))


    # Order Pet
    order1 = Order(
        id = 2,
        petId= 2,
        quantity= 1,
    )

    # Order Pet
    print("=" * 20 + "Order Pet" + "=" * 20)
    response_pet_order = store_api.order_pet(order1)
    print(json.dumps(response_pet_order.json(), indent=4))


    # GET ORDER BY ID
    print("=" * 20 + "GET ORDER STATUS" + "=" * 20)
    response_order_status = store_api.get_by_order_id(3)
    print(json.dumps(response_order_status.json(), indent=4))

    # DELETE ORDER BY ID
    print("=" * 20 + "DELETE ORDER" + "=" * 20)
    response_order_delete = store_api.get_by_order_id(5)
    print(json.dumps(response_order_delete.json(), indent=4))