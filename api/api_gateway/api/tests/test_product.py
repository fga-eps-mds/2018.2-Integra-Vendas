from django.test import TestCase
from .product_test_helper import create_product
from .login_test_helper import registrate_new_user, login_user

default_name = "test1234"
default_fk_vendor = 1
default_price = '10.0'
default_photo = 'www.google.com'
default_description = 'description'

# Create your tests here.
class ProductTest(TestCase):
    def test_product_creation_with_valid_params(self):
        email = 'teste123@teste.com'
        
        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        login_token = loginResponseJson["token"]
        fk_vendor = loginResponseJson["user"]["pk"]

        data = create_product(default_name, fk_vendor, default_price, default_photo, default_description, login_token)
        response = self.client.post('/api/create_product/', data=data)

        self.assertEqual(response.status_code, 200)

    def test_product_creation_with_invalid_params(self):
        email = 'teste321@teste.com'

        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        fk_vendor = loginResponseJson["user"]["pk"]

        data = create_product(default_name, fk_vendor, default_price, default_photo, default_description)
        response = self.client.post('/api/create_product/', data=data)

        self.assertEqual(response.status_code, 403)