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
from .response_helper import default_response

@api_view(["POST"])
def create_order(request):
    return default_response(settings.ORDER + '/api/create_order/', request)

@api_view(["POST"])
def set_order_status(request):
    return default_response(settings.ORDER + '/api/set_order_status/', request)

@api_view(["POST"])
def buyer_orders(request):
    return default_response(settings.ORDER + '/api/buyer_orders/', request)