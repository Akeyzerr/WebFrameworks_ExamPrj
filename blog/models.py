from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from storages.backends.s3boto3 import S3Boto3Storage

from users.models import Profile


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="posts_imgs", storage=S3Boto3Storage())
    content = RichTextField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)  # original timestamp
    date_edited = models.DateTimeField(auto_now=True)  # updated on Model.save()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['-date_edited']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            slug = slugify(self.title)
            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '_' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)

    def absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class PostComment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_body = models.TextField(blank=True, null=True)
    comment_posted_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_body
