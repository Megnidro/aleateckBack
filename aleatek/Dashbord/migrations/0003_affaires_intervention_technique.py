# Generated by Django 4.2 on 2023-05-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0004_interventiontechniques_and_more'),
        ('Dashbord', '0002_remove_affaires_intervention_technique'),
    ]

    operations = [
        migrations.AddField(
            model_name='affaires',
            name='intervention_technique',
            field=models.ManyToManyField(to='IT.interventiontechniqueassocie'),
        ),
    ]