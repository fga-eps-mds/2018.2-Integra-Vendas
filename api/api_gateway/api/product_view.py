from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.conf import settings
from .response_healper import default_response

@api_view(["POST"])
def create_product(request):
    url = settings.PRODUCTS + '/api/create_product/'
    return default_response(url, request)

@api_view(["POST"])
def all_products(request):
    url = settings.PRODUCTS + '/api/all_products/'
    return default_response(url, request)

@api_view(["POST"])
def my_products_screen(request):
    url = settings.PRODUCTS + '/api/user_products/'
    return default_response(url, request)

@api_view(["POST"])
def get_product(request):
    url = settings.PRODUCTS + '/api/get_product/'
    return default_response(url, request)

@api_view(["POST"])
def edit_product(request):
    url = settings.PRODUCTS + '/api/edit_product/'
    return default_response(url, request)

@api_view(["POST"])
def delete_product(request):
    url = settings.PRODUCTS + '/api/delete_product/'
    return default_response(url, request)