from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings

def get_version(name):
    general_timeout = 2
    url = get_url(name)
    if(url == None) 
        return
        
    try:
        response = requests.get(url, timeout=general_timeout)
        response_json=response.json()
    except:
        response_json={
            "name": name,
            "online": False,
        }
    return response_json

def get_url(name)
    if name == "login-microservice":
        url = settings.LOGIN
    elif name == "product-microservice":
        url = settings.PRODUCTS
    elif name == "order-microservice":
        url = settings.ORDER
    elif name == "notification-microservice":
        url = settings.NOTIFICATION
    else:
        return None

    return url