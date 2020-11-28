from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    phone=models.CharField(max_length=11, unique=True)
    location=models.CharField(max_length=127)
    bio=models.TextField()

    # USERNAME_FIELD =('phone')
    # REQUIRED_FIELDS = ['phone']
