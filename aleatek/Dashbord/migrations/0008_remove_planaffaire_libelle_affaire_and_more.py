# Generated by Django 4.2 on 2023-05-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashbord', '0007_rename_affaire_planaffaire_libelle_affaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planaffaire',
            name='libelle_affaire',
        ),
        migrations.AddField(
            model_name='planaffaire',
            name='libelle_affaire',
            field=models.ManyToManyField(to='Dashbord.affaires'),
        ),
    ]
