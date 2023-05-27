# Generated by Django 4.2 on 2023-05-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0004_interventiontechniques_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interventiontechniqueassocie',
            old_name='code_chantier',
            new_name='cod_it',
        ),
        migrations.RemoveField(
            model_name='interventiontechniqueassocie',
            name='affectable',
        ),
        migrations.RemoveField(
            model_name='interventiontechniqueassocie',
            name='code_libelle',
        ),
        migrations.RemoveField(
            model_name='interventiontechniqueassocie',
            name='information',
        ),
        migrations.RemoveField(
            model_name='interventiontechniqueassocie',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='interventiontechniqueassocie',
            name='num_service_propose',
        ),
        migrations.AlterField(
            model_name='interventiontechniqueassocie',
            name='libelle_it',
            field=models.CharField(max_length=200),
        ),
    ]