# Generated by Django 4.2 on 2023-05-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashbord', '0019_alter_planaffaire_affaire_alter_planaffaire_produit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
