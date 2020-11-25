# Generated by Django 3.1.3 on 2020-11-25 01:49

import PyWEB_Exam2.storage_backend
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201125_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/profile/default.jpg', storage=PyWEB_Exam2.storage_backend.StaticStorage(), upload_to='profile_pics'),
        ),
    ]
