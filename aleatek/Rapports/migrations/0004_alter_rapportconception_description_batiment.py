# Generated by Django 4.2 on 2023-05-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0006_remove_destination_batiment_and_more'),
        ('Rapports', '0003_rapportconception_complement_titre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapportconception',
            name='description_batiment',
            field=models.ManyToManyField(to='destinations.destination'),
        ),
    ]