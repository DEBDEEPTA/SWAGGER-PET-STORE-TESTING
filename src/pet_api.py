from dataclasses import asdict
from utils.api_client import ApiClient
from src.models.pet import Pet
from src.models.category import Category
from src.models.tags import Tag
import json

class PetApi:
    def __init__(self):
        self.client = ApiClient("https://petstore.swagger.io/v2")

    def get_pet_by_id(self, pet_id: int):
        return self.client.get(f"/pet/{pet_id}")

    def get_pets_by_status(self, status: str):
        return self.client.get(
            "/pet/findByStatus",
            params={"status": status}
        )

    def create_pet(self, pet: Pet):
        payload = asdict(pet)

        return self.client.post(
            "/pet",
            json=payload
        )


    def update_pet(self, pet: Pet):
        payload = asdict(pet)
        return self.client.put(
            "/pet",
            json=payload
        )


    def delete_pet(self, pet_id: int):
        return self.client.delete(f"/pet/{pet_id}")

    def upload_pet_image(self, pet_id: int, meta_data: str, file_path: str):
        endpoint = f"/pet/{pet_id}/uploadImage"

        with open(file_path, "rb") as f:
            return self.client.post(
                endpoint,
                data={"additionalMetadata": meta_data},
                files={"file": (file_path, f, "image/png")}
            )


if __name__=="__main__":
    pet_api = PetApi()

    t1 =  Tag( id= 1,name= "puppy")
    t2 = Tag (id = 2, name="vacinated")
    my_pet = Pet(
        id=1,
        name="bholu",
        category= Category(
            id = 1,
            name= "Shiba"
        ),
        photoUrls= [r"C:\Users\krish\OneDrive\Pictures\Screenshots\Screenshot 2026-03-02 160755.png"],
        tags= [t1,t2],
        status= "available"
    )

    # FETCH PET BY ID
    print("=" * 20 + "FETCH PET BY ID" + "=" * 20)
    response_pet_id = pet_api.get_pet_by_id(2)
    print(json.dumps(response_pet_id.json() , indent=4))

    # FETCH PETS BY STATUS
    print("="*20+"AVAILABLE PETS"+"="*20)
    response_pet_by_status = pet_api.get_pets_by_status("available")
    print(json.dumps(response_pet_by_status.json(), indent=4))

    # CREATE A PET
    print("=" * 20 + "CREATE/POST A PET" + "=" * 20)
    response_create_pet = pet_api.create_pet(my_pet)
    print(json.dumps(response_create_pet.json(), indent=4))

    # UPDATE PET
    print("=" * 20 + "UPDATE A PET" + "=" * 20)
    response_update_pet = pet_api.update_pet(my_pet)
    print(json.dumps(response_update_pet.json(), indent=4))

    # DELETE PET

    print("=" * 20 + "DELETE A PET" + "=" * 20)
    response_delete_pet = pet_api.delete_pet(3)
    print(json.dumps(response_delete_pet.json(), indent=4))

    # UPLOAD PET IMAGE
    pet_id = 3
    meta_data = "stupid pet"
    file_path = r"C:\Users\krish\OneDrive\Pictures\Screenshots\Screenshot 2026-03-02 144504.png"

    print("=" * 20 + "UPLOAD PET IMAGE" + "=" * 20)
    response_upload_pet_img = pet_api.upload_pet_image(pet_id,meta_data, file_path)
    print(json.dumps(response_upload_pet_img.json(), indent=4))
