from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)   # original timestamp
    date_edited = models.DateTimeField(auto_now=True)   # updated on Model.save()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_edited']

    def __str__(self):
        return self.title

    def absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
