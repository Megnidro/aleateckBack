# Generated by Django 4.2 on 2023-05-25 03:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashbord', '0020_alter_produit_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='planaffaire',
            name='intervenant',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
