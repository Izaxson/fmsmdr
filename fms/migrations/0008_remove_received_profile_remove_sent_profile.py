# Generated by Django 4.2.4 on 2023-09-26 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0007_alter_sent_office_from'),
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
