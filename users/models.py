from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class User(AbstractBaseUser):

    email = models.EmailField(_("email address"), unique=True)
    is_admin = models.BooleanField (default=False)
    is_active = models.BooleanField (default=True)
    date_joined = models.DateTimeField (default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email