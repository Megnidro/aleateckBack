# Generated by Django 4.2 on 2023-05-25 04:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Document', '0013_remove_avis_num_avis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='collaborateurs',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
