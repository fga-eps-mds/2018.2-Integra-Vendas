from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def status(request):
    version=file_get_contents("../VERSION")
    print (version)
    return Response({
    "name":"api-gateway",
    "version":version,
    "services":[
        {
            "name": "login-microservice",
            "online": True,
            "version": "0.1"
        },
        {
            "name": "product-microservice",
            "online": True,
            "version": "0.1"
        },
        {
            "name": "order-microservice",
            "online": False
        }
    ],
})

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()
