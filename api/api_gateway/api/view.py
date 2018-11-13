from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.conf import settings
from .response_healper import default_response

@api_view(["POST"])
def get_name(request):
    url = settings.LOGIN + '/api/users/get_name/'
    return default_response(url, request)