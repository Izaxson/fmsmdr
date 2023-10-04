# Generated by Django 4.2.4 on 2023-09-30 10:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0015_remove_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[django.core.validators.FileExtensionValidator(['jpeg', 'jpg', 'gif', 'png'])]),
        ),
    ]
