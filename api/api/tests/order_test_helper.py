from django.conf import settings
import requests

def create_order(fk_product = None, fk_buyer = None, buyer_message = None, quantity = None, total_price = None, product_name = None, token = None):

    data = {
        'fk_product': fk_product,
        'fk_buyer': fk_buyer,
        'buyer_message': buyer_message,
        'quantity': quantity,
        'total_price': total_price,
        'product_name': product_name,
        'token': token
    }

    return data
