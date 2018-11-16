from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE
)
from rest_framework.response import Response
from .login_views import verify_token
import requests
import json
# from .cloudinary_helper import upload_image

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

# def create_product_response(url, request):
#     verify = verify_token(request.data)
#     if verify.status_code != 200:
#         return verify

#     DEFAULT_PRODUCT_IMAGE = 'https://res.cloudinary.com/integraappfga/image/upload/v1541537829/senk2odnxamopwlkmyoq.png'
#     product = request.data.dict()
#     photo = product.get("photo")
#     if (photo != None):
#         try:
#             photo_url = upload_image(product["photo"])
#             product.update({'photo': photo_url})
#         except:
#             return Response({'error': 'Não foi possível fazer o upload da imagem.'},
#                                     status=HTTP_503_SERVICE_UNAVAILABLE)
#     else:
#         product.update({'photo': DEFAULT_PRODUCT_IMAGE})

#     return default_response(settings.PRODUCTS + '/api/create_product/', data=product)

# def edit_product_response(url, request):
#     ## Verificação do token
#     verify = verify_token(request.data)
#     if verify.status_code != 200:
#         return verify

#     # Transforming request to python dictionary to treat photo
#     product = request.data.dict()
#     photo = product.get("photo")
#     if (photo != None):
#         try:
#             photo_url = upload_image(product["photo"])
#             product.update({'photo': photo_url})
#         except:
#             return Response({'error': 'Não foi possível fazer o upload da imagem.'},
#                                     status=HTTP_503_SERVICE_UNAVAILABLE)

#     # If there is no photo in request just do not send it to the microservice

#     return default_response(settings.PRODUCTS + '/api/edit_product/', data=product)
