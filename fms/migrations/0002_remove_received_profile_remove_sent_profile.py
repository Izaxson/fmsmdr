# Generated by Django 4.2.4 on 2023-09-24 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='received',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='sent',
            name='profile',
        ),
    ]
