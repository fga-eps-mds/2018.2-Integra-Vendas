from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests
from django.conf import settings
from .response_helper import default_response
from .cloudinary_helper import upload_image
from .login_views import verify_token

@api_view(["POST"])
def create_product(request):
    DEFAULT_PRODUCT_IMAGE = 'https://res.cloudinary.com/integraappfga/image/upload/v1541537829/senk2odnxamopwlkmyoq.png'
    
    product = request.data.dict()
    photo = product.get("photo")
    if (photo != None):
        try:
            photo_url = upload_image(product["photo"])
            product.update({'photo': photo_url})
        except:
            return Response({'error': 'Não foi possível fazer o upload da imagem.'},
                                    status=HTTP_503_SERVICE_UNAVAILABLE)
    else:
        product.update({'photo': DEFAULT_PRODUCT_IMAGE})
    
    return default_response(settings.PRODUCTS + '/api/create_product/', product)


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
    # Transforming request to python dictionary to treat photo
    product = request.data.dict()
    photo = product.get("photo")
    if (photo != None):
        try:
            photo_url = upload_image(product["photo"])
            product.update({'photo': photo_url})
        except:
            return Response({'error': 'Não foi possível fazer o upload da imagem.'},
                                    status=HTTP_503_SERVICE_UNAVAILABLE)

    # If there is no photo in request just do not send it to the microservice

    return default_response(settings.PRODUCTS + '/api/edit_product/', product)

@api_view(["POST"])
def delete_product(request):
    return default_response(settings.PRODUCTS + '/api/delete_product/', request)