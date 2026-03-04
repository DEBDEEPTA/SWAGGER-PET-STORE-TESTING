from utils.api_client import ApiClient
from src.models.user import User
from dataclasses import asdict
import json
class UserApi:
    def __init__(self):
        self.client = ApiClient("https://petstore.swagger.io/v2")

    def create_user(self, u:User):
        endpoint = "/user"
        payload = asdict(u)

        return self.client.post(endpoint=endpoint, json=payload)

    def create_user_list(self, u_list):
        endpoint = 'user/createWithlist'

        return self.client.post(endpoint=endpoint, json=u_list)

    def get_user_by_username(self, username:str):
        endpoint = f"/user{username}"
        return self.client.get(endpoint=endpoint)

    def login_user(self,username:str,password:str):
        endpoint = "/user/login"
        params = {
            'username':username,
            'password':password
        }
        return self.client.get(endpoint=endpoint,params=params)

    def logout_user(self):
        return self.client.get(endpoint="/user/logout")


    def update_user(self,username:str, u:User):
        endpoint = f"/user/{username}"
        payload = asdict(u)

        return self.client.put(endpoint=endpoint, json=payload)

    def delete_user(self,username:str):
        endpoint = f"/user/{username}"
        return self.client.delete(endpoint=endpoint)



if __name__=="__main__":
    user_api = UserApi()


    user1 = User(
        id = 3,
        username= "dev2oo3",
        firstName='Dev',
        lastName="S",
        email='askdev2003@gmail.com',
        phone='+91 8001334960',
        userStatus=0,
        password='Dev1234'
    )

    # CREATE USER
    print("=" * 20 + "CREATE USER" + "=" * 20)
    response_create_user = user_api.create_user(user1)
    print(json.dumps(response_create_user.json(), indent=4))

    # LOGIN USER
    print("=" * 20 + "LOGIN USER" + "=" * 20)
    response_user_login = user_api.login_user("dev2oo3","Dev1234")
    print(json.dumps(response_user_login.json(), indent=4))



