# Generated by Django 3.1.3 on 2020-12-10 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201205_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tasks_per_page',
            field=models.IntegerField(default=3),
        ),
    ]
