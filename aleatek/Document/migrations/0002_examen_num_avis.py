# Generated by Django 4.2 on 2023-05-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='num_avis',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
