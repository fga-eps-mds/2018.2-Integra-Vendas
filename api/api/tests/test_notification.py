from django.test import TestCase
from .login_test_helper import registrate_new_user, login_user

default_user_token = 'NotValidToken'

# Create your tests here.
class NotificationTest(TestCase):
    def test_user_token_save(self):
        email = 'testeNotification@teste.com'

        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        login_token = loginResponseJson["token"]
        user_id = loginResponseJson["user"]["pk"]

        data = {'user_token': default_user_token, 'user_id': user_id, 'token': login_token}
        response = self.client.post('/api/save_user_token/', data=data)

        self.assertEqual(response.status_code, 200)

    def test_forbidden_token_save(self):
        data = {'user_token': default_user_token, 'user_id': 1, 'token': 'NotValidToken'}
        response = self.client.post('/api/save_user_token/', data=data)

        self.assertEqual(response.status_code, 403)

    def test_send_push_messaage(self):
        email = 'testeNotification@teste.com'

        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        login_token = loginResponseJson["token"]
        user_id = loginResponseJson["user"]["pk"]

        data = {'title': 'ThisIsATitle', 'message': 'ThisIsAMessage', 'user_id': user_id, 'token': login_token}
        response = self.client.post('/api/send_push_message/', data=data)

        self.assertEqual(response.status_code, 200)

    def test_forbidden_push_message(self):
        data = {'title': 'ThisIsATitle', 'message': 'ThisIsAMessage', 'user_id': 1, 'token': 'NotValidToken'}
        response = self.client.post('/api/send_push_message/', data=data)

        self.assertEqual(response.status_code, 403)
