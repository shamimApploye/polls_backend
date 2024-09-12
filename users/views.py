from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
class UsersList (APIView):
    def get (self, req):
        return Response ('ok')
    def post (self, req):
        return Response ('ok')

class UsersDetail (APIView):
    def get (self, req, id):
        return Response ('ok')
    def put (self, req, id):
        return Response ('ok')
    def delete (self, req, id):
        return Response ('ok')