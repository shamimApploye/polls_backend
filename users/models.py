from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField (max_length= 255, unique= True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ "first_name", "last_name"]

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)

