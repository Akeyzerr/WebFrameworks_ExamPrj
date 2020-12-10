from django.db import models
from django.contrib.auth.models import User
from PyWEB_Exam2.storage_backend import *
from .validators import *
from django.contrib.auth.validators import UnicodeUsernameValidator


class Profile(models.Model):
    QUOTES_CHOICES = (
        (True, "Yes"),
        (False, "No"),)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='/profile/default.jpg', upload_to='profile_pics', storage=S3Boto3Storage())
    clean_quote_of_the_day = models.BooleanField(choices=QUOTES_CHOICES, default=False)
    tasks_per_page = models.IntegerField(default=3)
    blogposts_per_page = models.IntegerField(default=3)

    def __str__(self):
        return f'{self.user.username} Profile'

    # TODO: Image resize on profile.save() doesn't work because of the custom backend storage driver.
    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
