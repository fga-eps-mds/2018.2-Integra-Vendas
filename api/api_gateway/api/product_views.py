from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests
from django.conf import settings
from .response_helper import default_response
from .cloudinary_helper import update_photo
from .login_views import verify_token

@api_view(["POST"])
def create_product(request):
    # Transforming request to python dictionary to treat photo
    product = request.data.dict()
    need_default=True
    return update_photo(settings.PRODUCTS + '/api/create_product/', product, need_default)


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
    need_default=False
    # Transforming request to python dictionary to treat photo
    product = request.data.dict()
    return update_photo(settings.PRODUCTS + '/api/edit_product/', product, need_default)


@api_view(["POST"])
def delete_product(request):
    return default_response(settings.PRODUCTS + '/api/delete_product/', request)