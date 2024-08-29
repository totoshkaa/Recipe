from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users-images/', default='default_profile_picture.jpg')

    def __str__(self):
        return str(self.username)