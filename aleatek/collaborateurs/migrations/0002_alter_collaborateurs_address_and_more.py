# Generated by Django 4.2 on 2023-05-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborateurs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateurs',
            name='address',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='city',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='country',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='implantation',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='nom',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='prenom',
            field=models.CharField(max_length=15, verbose_name='Prénoms'),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='state',
            field=models.CharField(max_length=15),
        ),
    ]