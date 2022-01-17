from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='static/Profile_pics', null=True, default="static/default.jpg")