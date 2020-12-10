from django.contrib.auth.models import User
from django.db import models
from django_currentuser.middleware import get_current_authenticated_user

from blog.models import Tag


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_authenticated_user)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'{self.title}'
