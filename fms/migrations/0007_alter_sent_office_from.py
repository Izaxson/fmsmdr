# Generated by Django 4.2.4 on 2023-09-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0006_remove_received_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sent',
            name='office_from',
            field=models.CharField(choices=[('Office of The Governor', 'Office of The Governor'), ('Office_of_The_Deputy_Governor', 'Office of The Deputy Governor')], max_length=200),
        ),
    ]
