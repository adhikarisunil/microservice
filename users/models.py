from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=[]

    objects = UserManager()

    def __str__(self):
        return self.username
