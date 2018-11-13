from django.conf import settings
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.response import Response
import requests
import json
from rest_framework.decorators import api_view

def verify_token(data_request):
    if not 'token' in data_request:
        return Response({'error': 'Token vazio'},
                                status=HTTP_400_BAD_REQUEST)
    try:
        token = data_request['token']
        response = requests.post(settings.LOGIN + '/api/token-verify/', data={'token':token})
        if not 'token' in response.json():
            return Response({'error': 'Falha na autenticação'},
                                    status=HTTP_403_FORBIDDEN)
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor para autenticação'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({''}, HTTP_200_OK)
