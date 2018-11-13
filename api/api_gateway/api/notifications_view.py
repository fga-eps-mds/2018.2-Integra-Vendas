from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.conf import settings
from .response_healper import default_response

@api_view(["POST"])
def save_user_token(request):
    url = settings.NOTIFICATION + '/api/save_user_token/'
    return default_response(url, request)

@api_view(["POST"])
def send_push_message(request):
    url = settings.NOTIFICATION + '/api/send_push_message/'
    return default_response(url, request)