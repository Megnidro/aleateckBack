# Generated by Django 4.2 on 2023-04-18 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='date_of_birth',
        ),
    ]
