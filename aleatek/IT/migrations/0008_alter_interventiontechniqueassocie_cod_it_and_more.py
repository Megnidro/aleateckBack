# Generated by Django 4.2 on 2023-05-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0007_prestatationassocie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interventiontechniqueassocie',
            name='cod_it',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='interventiontechniqueassocie',
            name='libelle_it',
            field=models.CharField(max_length=20),
        ),
    ]
