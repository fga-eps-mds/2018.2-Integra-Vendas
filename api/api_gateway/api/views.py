from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE
)
from rest_framework.response import Response
import requests
import json
from django.conf import settings
from .login_helper import verify_token
import cloudinary.uploader

ORDER_CLOSED = 1
DEFAULT_PRODUCT_IMAGE = 'https://res.cloudinary.com/integraappfga/image/upload/v1541537829/senk2odnxamopwlkmyoq.png'

# Create your views here.
@api_view(["POST"])
def save_user_token(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.NOTIFICATION + '/api/save_user_token/', data= request.data)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def send_push_message(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.NOTIFICATION + '/api/send_push_message/', data= request.data)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def delete_product(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.PRODUCTS + '/api/delete_product/', data= request.data)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)

    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_order(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.ORDER + '/api/create_order/', data=request.data)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)

    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_product(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
        return verify

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
    else:
        product.update({'photo': DEFAULT_PRODUCT_IMAGE})

    try:
        response = requests.post(settings.PRODUCTS + '/api/create_product/', data=product)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)
    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def all_products(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.PRODUCTS + '/api/all_products/', data= request.data)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)


    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def my_products_screen(request):
    user_id = request.data.get('user_id')
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.PRODUCTS + '/api/user_products/', data={'user_id':user_id})
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)
    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def orders_screen(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        user_products = requests.post(settings.PRODUCTS + '/api/user_products/', data=request.data)
    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

    #Convert to JSon
    if user_products.status_code != 200:
        return Response(data=user_products.json(), status=user_products.status_code)

    #List to store all user orders
    all_user_orders = []
    for product in user_products.json():
        try:
            product_orders = requests.post(settings.ORDER + '/api/user_orders/', data={'product_id':product['id']})
        except:
            return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)
        orders = product_orders.json()
        for order in orders:
            if(order['status'] != ORDER_CLOSED):
                all_user_orders.append(order)

    return Response(data=all_user_orders, status=HTTP_200_OK)

@api_view(["POST"])
def get_product(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.PRODUCTS + '/api/get_product/', data= request.data)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)


    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def get_name(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.LOGIN + '/api/users/get_name/', data= request.data)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)


    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def set_order_status(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.ORDER + '/api/set_order_status/', data= request.data)
        return Response(response.json())
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                            status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def edit_product(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
        return verify

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

    try:
        response = requests.post(settings.PRODUCTS + '/api/edit_product/', data=product)
        try:
            response_json = json.loads(response.content)
            return Response(data=response_json)
        except:
            return Response(response)
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def buyer_orders(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    try:
        response = requests.post(settings.ORDER + '/api/buyer_orders/', data=request.data)
        return Response(data=response.json(), status=response.status_code)

    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},status=HTTP_500_INTERNAL_SERVER_ERROR)

def upload_image(photo):
    if (photo != None):
        upload_photo = cloudinary.uploader.upload(photo, 
            transformation = [
                {'width': 600, 'height': 350, 'crop': 'fit'}, 
            ]
        )
        photo_url = upload_photo['url']

    return photo_url
