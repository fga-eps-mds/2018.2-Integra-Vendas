from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE
)
from rest_framework.response import Response
from .login_views import verify_token
import requests
import json

def default_response(url, request):
    verify = verify_token(request.data)
    if verify.status_code != 200:
        return verify

    try:
        response = requests.post(url, data= request.data)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'}, status=HTTP_500_INTERNAL_SERVER_ERROR)