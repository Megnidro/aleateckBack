# Generated by Django 4.2 on 2023-05-30 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0028_remove_documents_nos_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avis',
            name='commentaire',
            field=models.ManyToManyField(blank=True, to='Document.commentaire'),
        ),
    ]