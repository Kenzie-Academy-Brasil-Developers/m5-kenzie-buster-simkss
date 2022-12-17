from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    birthdate = models.CharField(null=True, max_length=20)
    is_employee = models.BooleanField(default=False, null=True)
# Create your models here.
