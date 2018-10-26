from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings

@api_view(['GET'])
def status(request):
    general_timeout = 2
    
    ##Get login microservice version
    try:
        response = requests.get(settings.LOGIN, timeout=general_timeout)
        login_json=response.json()
    except:
        login_json={
            "name": "login-microservice",
            "online": False,
        }
    #Get product microservice version
    try:
        response = requests.get(settings.PRODUCTS, timeout=general_timeout)
        product_json=response.json()
    except:
        product_json={
            "name": "product-microservice",
            "online": False,
        }
    #Get order microservice version
    try:
        response = requests.get(settings.ORDER, timeout=general_timeout)
        order_json=response.json()
    except:
        order_json={
            "name": "order-microservice",
            "online": False,
        }

    return Response({
    "name":"api-gateway",
    "version":settings.VERSION,
    "services":[
        login_json,
        product_json,
        order_json,
    ],
})
