from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
class UsersList (APIView):
    def get (self, req):
        queryset = User.objects.all()
        serializer = UserSerializer (queryset, many = True)
        return Response (serializer.data)
    
    #  As an admin I can't create new user
    """
    def post (self, req):
        serializer = UserSerializer(data= req.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        print (serializer.data)
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    """

class UsersDetail (APIView):
    def get (self, req, id):
        user = get_object_or_404 (User, id = id)
        serializer = UserSerializer (user)
        return Response (serializer.data)
    
    #  As an admin i can't update an user
    """
    def put (self, req, id):
        user = get_object_or_404 (User, id = id)
        serializer = UserSerializer (user, data = req.data)
        serializer.is_valid(raise_exception= True) 
        serializer.save()
        return Response (serializer.data)
    """
    
    def delete (self, req, id):
        user = get_object_or_404 (User, id = id)
        user.delete()
        return Response ("Delete Done", status= status.HTTP_204_NO_CONTENT)