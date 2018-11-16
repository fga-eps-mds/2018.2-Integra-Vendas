from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from .version_helper import get_version

@api_view(['GET'])
def status(request):
    general_timeout = 2
    login_json = get_version("login-microservice")
    product_json = get_version("product-microservice")
    order_json = get_version("order-microservice")
    notification_json = get_version("notification-microservice")

    return Response({
    "name":"api-gateway",
    "version":settings.VERSION,
    "services":[
        login_json,
        product_json,
        order_json,
        notification_json,
    ],
})
