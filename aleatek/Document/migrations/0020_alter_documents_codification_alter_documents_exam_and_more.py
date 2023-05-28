# Generated by Django 4.2 on 2023-05-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0008_alter_interventiontechniqueassocie_cod_it_and_more'),
        ('Document', '0019_commentaire_remove_avis_a_suivre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='codification',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('RMQ', 'RMQ'), ('FA', 'FA'), ('HM', 'HM'), ('SO', 'SO'), ('VI', 'VI')], max_length=3),
        ),
        migrations.AlterField(
            model_name='documents',
            name='exam',
            field=models.ManyToManyField(blank=True, to='Document.avis'),
        ),
        migrations.AlterField(
            model_name='intervenantinterventiondocument',
            name='intervention_technique',
            field=models.ManyToManyField(blank=True, to='IT.interventiontechniqueassocie'),
        ),
    ]
