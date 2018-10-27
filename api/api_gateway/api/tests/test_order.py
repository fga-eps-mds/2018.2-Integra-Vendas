from django.test import TestCase
from .product_test_helper import create_product
from .order_test_helper import create_order
from .login_test_helper import registrate_new_user, login_user
import json

#Default order screen
default_fk_product = 1
default_fk_buyer = 1
default_buyer_message = 'default'
default_quantity = 1
default_total_price = 10.0
default_product_name = 'teste123'
default_order_id = 1
default_new_status = 0

#Default product screen
default_name = "test1234"
default_fk_vendor = 1
default_price = 10.0
default_photo = 'www.google.com'
default_description = 'description'
default_product_id = 1

# Create your tests here.
class OrderTest(TestCase):
    def test_order_creation_with_valid_params(self):
        #Vendor user
        email = 'teste004@teste.com'

        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        login_token = loginResponseJson["token"]
        fk_vendor = loginResponseJson["user"]["pk"]

        data = create_product(default_name, fk_vendor, default_price, default_photo, default_description, login_token)
        response = self.client.post('/api/create_product/', data=data)

        #Buyer user
        email2 = 'teste005@teste.com'

        responseJson2 = registrate_new_user(email2)
        loginResponseJson2 = login_user(email2)

        login_token2 = loginResponseJson["token"]
        fk_buyer2 = loginResponseJson["user"]["pk"]

        data2 = {'user_id': fk_vendor,'token': login_token}
        response2 = self.client.post('/api/my_products_screen/', data=data2)
        fk_product = response2.data[0]["id"]

        data3 = create_order(fk_product, fk_buyer2, default_buyer_message, default_quantity, default_total_price, default_product_name, login_token2)
        response3 = self.client.post('/api/create_order/', data=data3)

        self.assertEqual(response3.status_code, 200)

    def test_order_creation_with_invalid_params(self):
        data = {
            'fk_product': default_fk_product,
            'fk_buyer': default_fk_buyer,
            'buyer_message': default_buyer_message,
            'quantity': default_quantity,
            'total_price': default_total_price,
            'product_name': default_product_name,
            'token': None
        }

        response = self.client.post('/api/create_order/', data=data)

        self.assertEqual(response.status_code, 403)


    def test_set_order_status_with_invalid_params(self):
        data = {
            'order_id': default_order_id,
            'new_status': default_fk_buyer,
            'token': None
        }

        response = self.client.post('/api/set_order_status/', data=data)

        self.assertEqual(response.status_code, 403)

    def test_set_order_status_with_valid_params(self):
        email = 'teste006@teste.com'

        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        login_token = loginResponseJson["token"]
        fk_vendor = loginResponseJson["user"]["pk"]

        data = {'user_id': fk_vendor,'token': login_token}
        response = self.client.post('/api/my_products_screen/', data=data)

        data2 = create_order(default_fk_product, default_fk_buyer, default_buyer_message, default_quantity, default_total_price, default_product_name, login_token)
        response2 = self.client.post('/api/create_order/', data=data2)

        data3 = {
            'order_id': fk_vendor,
            'new_status': default_new_status,
            'token': login_token
        }

        response3 = self.client.post('/api/set_order_status/', data=data3)

        self.assertEqual(response3.status_code, 200)
