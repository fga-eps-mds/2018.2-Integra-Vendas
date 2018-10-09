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
    ## Verificação do token
    verify = verify_token(request.data)
    if not verify:
         return Response({'error': 'Falha na autenticacao'}, HTTP_403_FORBIDDEN)

    try:
        response = requests.post(settings.PRODUCTS + '/api/delete_product/', data= request.data)
        try:
            response_json = json.loads(response.content)
            return Response(data=response_json)
        except:
            return Response(response)
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_order(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if not verify:
         return Response({'error': 'Falha na autenticação'}, HTTP_403_FORBIDDEN)

    try:
        response = requests.post(settings.ORDER + '/api/create_order/', data=request.data)
        try:
            #Convert to JSon
            response_json = data=json.loads(response.content)
            return Response(data=response_json)

        except:
            return Response(response)

    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_product(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if not verify:
         return Response({'error': 'Falha na autenticação'}, HTTP_403_FORBIDDEN)

    try:
        response = requests.post(settings.PRODUCTS + '/api/create_product/', data= request.data)
        try:
            #Convert to JSon
            response_json = data=json.loads(response.content)
            return Response(data=response_json)

        except:
            return Response(response)
    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def all_products(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if not verify:
         return Response({'error': 'Falha na autenticação'}, HTTP_403_FORBIDDEN)

    try:
        response = requests.post(settings.PRODUCTS + '/api/all_products/', data= request.data)
        try:
            #Convert to JSon
            response_json = data=json.loads(response.content)
            return Response(data=response_json)

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
    if not verify:
         return Response({'error': 'Falha na autenticação'}, HTTP_403_FORBIDDEN)

    try:
        user_products = requests.post(settings.PRODUCTS + '/api/user_products/', data={'user_id':user_id})
        return Response(data=json.loads(user_products.content))
    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def orders_screen(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if not verify:
         return Response({'error': 'Falha na autenticação'}, HTTP_403_FORBIDDEN)

    try:
        user_products = requests.post(settings.PRODUCTS + '/api/user_products/', data=request.data)
    except:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

    #Convert to JSon
    user_products_response = Response(data=json.loads(user_products.content))

    #List to store all user orders
    all_user_orders = []

    for product in user_products_response.data:
        try:
            product_orders = requests.post(settings.ORDER + '/api/user_orders/', data={'product_id':product['id']})
        except:
            return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)
        orders = json.loads(product_orders.content)
        for order in orders:
            if(order['closed'] == False):
                all_user_orders.append(order)

    response = Response(data=all_user_orders)
    return response

def verify_token(data_request):

    if not 'token' in data_request:
        return False #Erro de token vazio

    try:
        token = data_request['token']
        response = requests.post(settings.LOGIN + '/api/token-verify/', data={'token':token})
        token_response = json.loads(response.content)
        if not 'token' in token_response:
            return False #Erro de token incorreto
    except:
        return False #Erro inesperado

    return True #Token cor

@api_view(["POST"])
def get_product(request):
    ## Verificação do token
    verify = verify_token(request.data)
    if not verify:
         return Response({'error': 'Falha na autenticação'}, HTTP_403_FORBIDDEN)

    try:
        response = requests.post(settings.PRODUCTS + '/api/get_product/', data= request.data)
        try:
            response_json = json.loads(response.content)
            return Response(data=response_json)
        except:
            return Response(response)
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)