from rest_framework import serializers as s
from .models import User
class UserSerializer (s.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "full_name", "is_staff" ]

    full_name = s.SerializerMethodField (method_name= 'get_full_name')

    def get_full_name (self, user:User):
        return (user.first_name + ' ' + user.last_name)
    
