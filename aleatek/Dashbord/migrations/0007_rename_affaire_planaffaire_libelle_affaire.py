# Generated by Django 4.2 on 2023-05-12 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashbord', '0006_rename_numero_affaire_planaffaire_affaire_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planaffaire',
            old_name='affaire',
            new_name='libelle_affaire',
        ),
    ]
