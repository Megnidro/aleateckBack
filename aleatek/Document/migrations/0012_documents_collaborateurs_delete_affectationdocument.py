# Generated by Django 4.2 on 2023-05-25 03:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Document', '0011_merge_20230525_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='collaborateurs',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='AffectationDocument',
        ),
    ]