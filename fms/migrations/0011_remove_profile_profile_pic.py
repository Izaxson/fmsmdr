# Generated by Django 4.2.4 on 2023-09-29 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0010_profile_is_admin_profile_is_clerk_profile_is_deputy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]
