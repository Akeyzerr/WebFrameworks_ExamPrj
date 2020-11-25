from abc import ABC
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
class StaticStorage(S3Boto3Storage, ABC):
    location = settings.AWS_STATIC_LOCATION


class PublicMediaStorage(S3Boto3Storage, ABC):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage, ABC):
    """Uploads a file to a private space in the AWS bucket.
        Later only accessible via AWS generated link with custom ttl.
        IDK if I'll use this in the exam project."""
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
