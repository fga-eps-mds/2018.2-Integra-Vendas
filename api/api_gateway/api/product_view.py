from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.conf import settings
from .response_helper import default_response

@api_view(["POST"])
def create_product(request):
    return default_response(settings.PRODUCTS + '/api/create_product/', request)

@api_view(["POST"])
def all_products(request):
    return default_response(settings.PRODUCTS + '/api/all_products/', request)

@api_view(["POST"])
def my_products_screen(request):
    return default_response(settings.PRODUCTS + '/api/user_products/', request)

@api_view(["POST"])
def get_product(request):
    return default_response(settings.PRODUCTS + '/api/get_product/', request)

@api_view(["POST"])
def edit_product(request):
    return default_response(settings.PRODUCTS + '/api/edit_product/', request)

@api_view(["POST"])
def delete_product(request):
    return default_response(settings.PRODUCTS + '/api/delete_product/', request)