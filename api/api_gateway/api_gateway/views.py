from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings

@api_view(['GET'])
def status(request):
    
    ##Get login microservice version
    try:
        response = requests.get(settings.LOGIN)
        login_json=response.json()
    except:
        login_json={
            "name": "login-microservice",
            "online": False,
        }
    #Get product microservice version
    try:
        response = requests.get(settings.PRODUCTS)
        product_json=response.json()
    except:
        product_json={
            "name": "product-microservice",
            "online": False,
        }
    #Get order microservice version
    try:
        response = requests.get(settings.ORDER)
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
