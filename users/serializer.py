from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()  # Correct usage of SerializerMethodField

    class Meta:
        model = User
        fields = ['id', 'full_name', "email","password", "first_name", "last_name", 'is_staff']  # Fields to expose in the API response
        read_only_fields = ['id', 'full_name', 'is_staff']  # Fields that should be read-only
        extra_kwargs = {
            "first_name": {'write_only': True}, 
            "last_name": {'write_only': True},
            "password": {'write_only': True},
        }

    def get_full_name(self, user: User):
        return f"{user.first_name} {user.last_name}"
