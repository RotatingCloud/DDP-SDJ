from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD='username'
                                   