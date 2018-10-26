from django.conf import settings
import requests

def create_product(name, fk_vendor, price, photo, description, token):

    data = {
        'fk_vendor': fk_vendor,
        'name': name,
        'price': price,
        'photo': photo,
        'description': description,
        'token': token
    }

    return data