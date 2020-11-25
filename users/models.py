from django.db import models
from django.contrib.auth.models import User
from PyWEB_Exam2.storage_backend import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='/profile/default.jpg', upload_to='profile_pics', storage=S3Boto3Storage())

    def __str__(self):
        return f'{self.user.username} Profile'
