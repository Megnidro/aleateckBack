# Generated by Django 4.2 on 2023-05-24 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborateurs', '0008_collaborateurs_poste_occupe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborateurs',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='collaborateurs',
            name='user',
        ),
    ]
