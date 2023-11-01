from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)