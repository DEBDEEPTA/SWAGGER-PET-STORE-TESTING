import pytest
from src.user_api import UserApi
from src.models.user import User
@pytest.fixture
def user_api():
    return UserApi()

@pytest.fixture
def user_factory():
    def create_user(id: int,
                    username: str,
                    firstName: str,
                    lastName: str,
                    email: str,
                    password: str,
                    phone: str,
                    userStatus: int
                    ):

        new_user = User(id,username,firstName,lastName,email,password,phone,userStatus)
        return new_user
    return create_user