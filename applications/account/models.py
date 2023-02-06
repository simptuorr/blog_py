from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    username = None
    activation_code = models.CharField(max_length=50,blank=True)

    ...

    def __str__(self):
        return self.email

