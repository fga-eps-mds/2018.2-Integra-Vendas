from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def status(request):
    title = "message"
    message = "Hello for today! See you tomorrow!"
    return Response({title: message})
