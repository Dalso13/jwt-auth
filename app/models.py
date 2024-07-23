import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=200, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=True)

