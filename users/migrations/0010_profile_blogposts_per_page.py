# Generated by Django 3.1.3 on 2020-12-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_tasks_per_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blogposts_per_page',
            field=models.ImageField(default=3, upload_to=''),
        ),
    ]
