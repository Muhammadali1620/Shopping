from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import CustomUserManager
from apps.users.validate import phone_number_validate


class CustomUser(AbstractUser):
    username = None

    objects = CustomUserManager()

    phone_number = models.CharField(max_length=13, validators=[phone_number_validate], unique=True)
    full_name = models.CharField(max_length=75)

    USERNAME_FIELD = 'phone_number'
