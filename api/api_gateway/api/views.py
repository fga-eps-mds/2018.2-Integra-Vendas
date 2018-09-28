from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.response import Response
import requests
import json
from django.conf import settings

# Create your views here.
@api_view(["POST"])
def delete_product(request):

    try:
        response = Response(requests.post(settings.PRODUCTS + '/api/delete_product', data= request.data))

        return response
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_order(request):
    token = request.data.get('token')
    auth = verify_token(token)
    
    if 'token' not in auth.data:
        return Response({'error': 'Erro de autenticacao'}, HTTP_403_FORBIDDEN)
        
    try:
        order = requests.post(settings.ORDER + '/api/create_order', data=request.data)
        try:
            order_response = Response(data=json.loads(order.content))
            print(order_response.data)
            response = Response(data=order_response.data)
            return Response(data=response.data)
        except:
            return Response(order)

    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_product(request):
    try:
        response = Response(requests.post(settings.PRODUCTS + '/api/create_product/', data= request.data))
        return response
    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def orders_screen(request):
    user_id = request.data.get('user_id')
    user_products = requests.post(settings.PRODUCTS + '/api/user_products', data={'user_id':user_id})
    #Convert to JSon
    user_products_response = Response(data=json.loads(user_products.content))

    #List to store all user orders
    all_user_orders = []

    for product in user_products_response.data:
        product_orders = requests.post(settings.ORDER + '/api/user_orders', data={'product_id':product['id']})
        orders = json.loads(product_orders.content)
        for order in orders:
            if(order['closed'] == False):
                all_user_orders.append(order)

    response = Response(data=all_user_orders)
    return response

def verify_token(token):
    if(token == None):
        return Response({'error': 'Erro de autenticacao, token vazio'},HTTP_400_BAD_REQUEST)
        
    response = requests.post(settings.LOGIN + '/api-token-verify/', data={'token':token})
    return Response(data=json.loads(response.content), status=HTTP_200_OK)