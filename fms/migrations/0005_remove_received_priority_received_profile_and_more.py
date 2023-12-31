# Generated by Django 4.2.4 on 2023-09-26 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0004_alter_received_entity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='received',
            name='priority',
        ),
        migrations.AddField(
            model_name='received',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='fms.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sent',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='fms.profile'),
            preserve_default=False,
        ),
    ]
