# Generated by Django 3.1.3 on 2020-12-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201125_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='clean_quote_of_the_day',
            field=models.CharField(choices=[('Yes', True), ('No', False)], default=False, max_length=10),
        ),
    ]