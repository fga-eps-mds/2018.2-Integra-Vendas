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