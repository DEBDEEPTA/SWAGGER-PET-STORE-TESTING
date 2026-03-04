import pytest

@pytest.mark.pet
class TestPetApi:

    @pytest.mark.parametrize("pet_id,pet_name",[(1,"bholu"),
                                                (2,"candy"),
                                                (3,'mimi'),
                                                (4,'golu'),
                                                (5,'rimi'),
                                                (6,'dholu')])
    def test_create_pet(self,pet_api,pet_factory,pet_id,pet_name):

        my_pet = pet_factory(pet_id=pet_id,pet_name=pet_name)
        response = pet_api.create_pet(my_pet)
        assert response.status_code == 200
        assert response.json()["id"] == my_pet.id
        assert response.json()["name"] == my_pet.name


    @pytest.mark.parametrize("pet_id",[1,2,3,4,5,6])
    def test_get_pet_by_id(self,pet_id,pet_api):
        response = pet_api.get_pet_by_id(pet_id)

        assert response.status_code == 200
        assert response.json()["id"] == pet_id


    @pytest.mark.parametrize("status",["available","pending","sold"])
    def test_get_pets_by_status(self,status,pet_api):
        response = pet_api.get_pets_by_status(status)

        assert response.status_code == 200
        assert len(response.json()) > 1

    @pytest.mark.parametrize("pet_id",[1,2,3,4])
    def test_delete_pet(self,pet_api,pet_id):
        response = pet_api.delete_pet(pet_id=pet_id)
        assert response.status_code == 200

    @pytest.mark.parametrize("pet_id,meta_data,file_path",[
        (5, "teat_img_1", r"C:\Users\krish\OneDrive\Pictures\Screenshots\Screenshot 2026-03-02 144504.png"),
        (6,"test_image_2",r"C:\Users\krish\OneDrive\Pictures\Screenshots\Screenshot 2026-03-02 115712.png")
    ])
    def test_update_pet_img(self,pet_id,meta_data,file_path,pet_api):
        response = pet_api.upload_pet_image(pet_id,meta_data,file_path)
        assert response.status_code == 200


