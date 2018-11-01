from django.test import TestCase
from .login_test_helper import registrate_new_user, login_user

default_user_id = 1

class UserTest(TestCase):
    def test_get_name_with_valid_params(self):
        email = 'teste999@teste.com'

        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        login_token = loginResponseJson["token"]
        user = loginResponseJson["user"]["pk"]

        data = {'user_id': user, 'token': login_token}
        response = self.client.post('/api/get_name/', data=data)

        self.assertEqual(response.data["name"], '')
        self.assertEqual(response.status_code, 200)

    def test_get_name_with_invalid_params(self):
        data = {'user_id': default_user_id, 'token': None}
        response = self.client.post('/api/get_name/', data=data)

        self.assertEqual(response.status_code, 403)