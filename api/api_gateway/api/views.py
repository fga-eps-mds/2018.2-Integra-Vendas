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

# Create your views here.
@api_view(["POST"])
def delete_product(request):
    try:
        response = Response(requests.post('http://192.168.15.9:8002/api/delete_product', data= request.data))
        return response
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_order(request):
    try:
        response = Response(requests.post('http://192.168.15.9:8001/api/create_order', data=request.data))
        return response
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)
