# Generated by Django 4.2 on 2023-05-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='media',
        ),
        migrations.AddField(
            model_name='media',
            name='name',
            field=models.CharField(default='name', max_length=15),
        ),
        migrations.AlterField(
            model_name='media',
            name='complement',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='media',
            name='identification',
            field=models.CharField(max_length=25),
        ),
    ]
