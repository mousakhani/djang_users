from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class CustomUser(AbstractUser):
    class Meta:
        # email became unique
        unique_together = ('email',)

    phone = models.CharField(max_length=11, null=True, blank=True)
    location = models.CharField(max_length=127, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # USERNAME_FIELD =('phone')

    # for reset password
    REQUIRED_FIELDS = ['email']
