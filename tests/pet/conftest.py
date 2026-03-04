import pytest
from src.models.category import Category
from src.models.tags import Tag
from src.pet_api import PetApi
from src.models.pet import Pet


@pytest.fixture(scope="class")
def pet_api():
    return PetApi()

@pytest.fixture
def pet_factory():
    def create_pet(pet_id,pet_name):
        t1 = Tag(id=1, name="puppy")
        t2 = Tag(id=2, name="vacinated")
        my_pet = Pet(
            id=pet_id,
            name=pet_name,
            category=Category(
                id=1,
                name="Shiba"
            ),
            photoUrls=[r"C:\Users\krish\OneDrive\Pictures\Screenshots\Screenshot 2026-03-02 160755.png"],
            tags=[t1, t2],
            status="available"
        )
        return my_pet
    return create_pet