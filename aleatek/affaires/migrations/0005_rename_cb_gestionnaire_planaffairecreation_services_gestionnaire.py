# Generated by Django 4.2 on 2023-05-01 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affaires', '0004_alter_planaffairecreation_numero_contrat_provisoire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planaffairecreation',
            old_name='cb_gestionnaire',
            new_name='services_gestionnaire',
        ),
    ]
