from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.response import Response
import requests
import json
from django.conf import settings
from .login_view import verify_token
from .response_healper import default_response

@api_view(["POST"])
def create_order(request):
    url = settings.ORDER + '/api/create_order/'
    return default_response(url, request)

@api_view(["POST"])
def set_order_status(request):
    url = settings.ORDER + '/api/set_order_status/'
    return default_response(url, request)

@api_view(["POST"])
def buyer_orders(request):
    url = settings.ORDER + '/api/buyer_orders/'
    return default_response(url, request)

@api_view(["POST"])
def orders_screen(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if verify.status_code != 200:
         return verify

    user_products = get_user_products(request.data)

    #Convert to JSon
    if user_products.status_code != 200:
        return Response(data=user_products.json(), status=user_products.status_code)

    #List to store all user orders
    all_user_orders = get_user_orders(user_products.json())

    if all_user_orders == 500:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                            status=HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(data=all_user_orders, status=HTTP_200_OK)

def get_user_products(data):
    try:
        user_products = requests.post(settings.PRODUCTS + '/api/user_products/', data=data)
        return user_products
    except:
        return 500

def get_user_orders(user_products):
    for product in user_products:
        try:
            product_orders = requests.post(settings.ORDER + '/api/user_orders/', data={'product_id':product['id']})
        except:
            return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)
        orders = product_orders.json()
        all_user_orders = get_product_orders(orders)
    return all_user_orders

def get_product_orders(orders):
    all_user_orders = []
    for order in orders:
        if(order['status'] != ORDER_CLOSED):
            all_user_orders.append(order)
    return all_user_orders