# Generated by Django 4.2 on 2023-05-25 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aso', '0010_alter_aso_aso_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aso',
            name='dossier',
        ),
    ]
