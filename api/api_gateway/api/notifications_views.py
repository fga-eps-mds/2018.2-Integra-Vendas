from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.conf import settings
from .response_helper import default_response

@api_view(["POST"])
def save_user_token(request):
    return default_response(settings.NOTIFICATION + '/api/save_user_token/', request)

@api_view(["POST"])
def send_push_message(request):
    return default_response(settings.NOTIFICATION + '/api/send_push_message/', request)