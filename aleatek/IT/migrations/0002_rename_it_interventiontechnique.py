# Generated by Django 4.2 on 2023-04-22 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborateurs', '0001_initial'),
        ('affaires', '0003_alter_planaffairecreation_debut_du_chantier_and_more'),
        ('missions', '0001_initial'),
        ('services', '0001_initial'),
        ('IT', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IT',
            new_name='InterventionTechnique',
        ),
    ]
