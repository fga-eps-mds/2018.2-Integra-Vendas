from django.test import TestCase
from .login_test_helper import registrate_new_user, login_user


# Create your tests here.
class LoginTest(TestCase):

    def test_user_registration(self):

        email = 'robson@hotmail.com'
        
        responseJson = registrate_new_user(email)

        token = responseJson['token']
        user = responseJson['user']

        self.assertEqual(user["email"], email)

    def test_user_login(self):

        email = 'serib@email.com'

        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        login_token = loginResponseJson["token"]
        user = loginResponseJson["user"]

        self.assertEqual(user["email"], email)

