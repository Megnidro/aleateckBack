# Generated by Django 4.2 on 2023-05-23 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0007_avis_remove_affectationitdocument_document_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avis',
            name='document',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='constructeurs',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='intervention_techniques',
        ),
        migrations.AddField(
            model_name='documents',
            name='exam',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Document.avis'),
            preserve_default=False,
        ),
    ]