from rest_framework.decorators import api_view
from django.conf import settings
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