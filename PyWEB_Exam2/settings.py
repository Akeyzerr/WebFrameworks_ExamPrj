import os
from os.path import join
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ["127.0.0.1",
                 "akeyzerr-exam2.herokuapp.com", ]

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'captcha',
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PyWEB_Exam2.urls'

USE_S3 = config("USE_S3", cast=bool)

if USE_S3:
    # Amazon Web Services Settings:
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_FILE_OVERWRITE = False

    # AWS S3 Staticfiles Settings
    AWS_STATIC_LOCATION = 'static'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'
    AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
    DEFAULT_FILE_STORAGE = 'PyWEB_Exam2.storage_backends.PublicMediaStorage'
    AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
    PRIVATE_FILE_STORAGE = 'PyWEB_Exam2.storage_backends.PrivateMediaStorage'

else:
    """this won't work at all; DO NOT USE or all hell breaks lose"""
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_URL = '/static/'

STATIC_ROOT = join(BASE_DIR, 'staticfiles/')
STATICFILES_DIRS = (join(BASE_DIR, "static/"),)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PyWEB_Exam2.wsgi.application'

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config("DB_NAME"),
    'USER': config("DB_USER"),
    'PASSWORD': config("DB_PASSWORD"),
    'HOST': config("DB_HOST"),
    'PORT': '5432'}}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

TIME_ZONE = 'Europe/Sofia'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'
