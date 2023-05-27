# Generated by Django 4.2 on 2023-05-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0001_initial'),
        ('affaires', '0005_rename_cb_gestionnaire_planaffairecreation_services_gestionnaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planaffairecreation',
            name='missions',
        ),
        migrations.AddField(
            model_name='planaffairecreation',
            name='missions',
            field=models.ManyToManyField(to='missions.missions'),
        ),
    ]