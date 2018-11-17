import cloudinary.uploader
from .login_views import verify_token
from rest_framework.response import Response
import requests
import json

def upload_image(photo):
    if (photo != None):
        upload_photo = cloudinary.uploader.upload(photo, 
            transformation = [
                {'width': 600, 'height': 350, 'crop': 'fit'}, 
            ]
        )
        photo_url = upload_photo['url']

    return photo_url

def update_photo(url, product, need_default):
    DEFAULT_PRODUCT_IMAGE = 'https://res.cloudinary.com/integraappfga/image/upload/v1541537829/senk2odnxamopwlkmyoq.png'

    verify = verify_token(product)
    if verify.status_code != 200:
        return verify

    photo = product.get("photo")
    if (photo != None):
        try:
            photo_url = upload_image(product["photo"])
            product.update({'photo': photo_url})
            
        except:
            return Response({'error': 'Não foi possível fazer o upload da imagem.'},
                                    status=HTTP_503_SERVICE_UNAVAILABLE)
    elif (need_default==True):
        product.update({'photo': DEFAULT_PRODUCT_IMAGE})

    try:
        response = requests.post(url, data=product)
        try:
            response_json = response.json()
            return Response(data=response_json, status=response.status_code)
        except:
            return Response(response)
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'}, status=HTTP_500_INTERNAL_SERVER_ERROR)