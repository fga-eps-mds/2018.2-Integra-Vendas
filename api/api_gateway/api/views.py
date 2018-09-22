from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.response import Response
import requests

# Create your views here.
@api_view(["POST"])
def delete_product(request):
    response = Response(requests.post('http://IP:8002/api/delete_product', data= request.data))
    return response
