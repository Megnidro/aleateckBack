# Generated by Django 4.2 on 2023-05-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborateurs', '0015_alter_collaborateurs_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborateurs',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
