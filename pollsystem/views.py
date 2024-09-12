from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def say_hello (req) :
    if req.method == 'GET':
        return Response ('Hello World')
    return Response ('not ok')