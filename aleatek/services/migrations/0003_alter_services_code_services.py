# Generated by Django 4.2 on 2023-05-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_services_code_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='code_services',
            field=models.IntegerField(),
        ),
    ]
