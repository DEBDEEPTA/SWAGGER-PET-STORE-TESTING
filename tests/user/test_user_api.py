import pytest

@pytest.mark.user
class TestUsers:

    @pytest.mark.parametrize(
        "id,username,firstName,lastName,email,password,phone,userStatus",
        [(1,"dev2oo3","Dev","Samui","deepo8@gmail.com","dev1234","+91 8001334960",0),
         (2,"Dhiru2oo3","Dhiraj","Kumar","dhiruvai@gmail.com","dhiru1234","+91 8489403967",1)]
    )
    def test_create_user(self,user_api,user_factory,id,username,firstName,lastName,email,password,phone,userStatus):
        new_user = user_factory(id,username,firstName,lastName,email,password,phone,userStatus)
        response = user_api.create_user(new_user)

        assert response.status_code == 200
        assert int(response.json()['message']) == id

    @pytest.mark.parametrize("username,password",[("dev2oo3","dev1234"),
                                                  ("Dhiru2oo3","dhiru1234")])
    def test_login_user(self,user_api,username,password):

        response = user_api.login_user(username,password)

        assert  response.status_code == 200


    @pytest.mark.parametrize(
        "id,username,firstName,lastName,email,password,phone,userStatus",
        [(2, "Dhiru2oo3", "Dhiraj", "Kumar", "dhiruvai2oo3@gmail.com", "dhiru1234", "+91 8489403967", 1)]
    )
    def test_update_user(self, user_api, user_factory, id, username, firstName, lastName, email, password, phone,
                         userStatus):
        updated_user = user_factory(id, username, firstName, lastName, email, password, phone, userStatus)
        response = user_api.update_user(username,updated_user)


    @pytest.mark.parametrize("username",["dev2oo3","Dhiru2oo3"])
    def test_delete_user(self,user_api,username):
        response = user_api.delete_user(username)

        assert  response.status_code == 200


