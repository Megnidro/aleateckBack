# Generated by Django 4.2 on 2023-05-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructeurs', '0002_entreprise_email'),
        ('Dashbord', '0010_alter_planaffaire_type_affaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='affaires',
            name='constructeurs',
            field=models.ManyToManyField(to='constructeurs.entreprise'),
        ),
    ]
