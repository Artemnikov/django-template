from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.EmailField(unique=True, validators=[EmailValidator(message="Enter a valid email address.")])
    phone_number = models.CharField(max_length=20, unique=True, null=True)
    avatar = models.FileField(upload_to="avatars/", null=True)
