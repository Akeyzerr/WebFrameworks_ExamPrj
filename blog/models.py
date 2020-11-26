from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    date_edited = models.DateTimeField(default=timezone.now) # can be modified later
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_edited']

    def __str__(self):
        return self.title

    def absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# class Document(models.Model):
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     upload = models.FileField()
#
#
# class PrivateDocument(models.Model):
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     upload = models.FileField(storage=PrivateMediaStorage())
#     user = models.ForeignKey(User, related_name='documents', on_delete=models.CASCADE)
