from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')), default='male')
    followers = models.ManyToManyField('self', through=Follow, symmetrical=False, related_name='following')
