from django.conf import settings
import requests

default_password = "test1234"

def registrate_new_user(email):
    
    data = {
        "username": email,
        "email": email,
        "password1": default_password,
        "password2": default_password
    }

    response = requests.post(settings.LOGIN + '/api/registration/', data=data)

    return response.json()

def login_user(email):

    data = {
        "username": email,
        "password": default_password
    }

    response = requests.post(settings.LOGIN + '/api/login/', data=data)

    return response.json()


