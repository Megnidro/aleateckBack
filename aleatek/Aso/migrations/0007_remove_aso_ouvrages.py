# Generated by Django 4.2 on 2023-05-12 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aso', '0006_rename_avis_ouvrages_aso_avis_ouvrage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aso',
            name='ouvrages',
        ),
    ]
