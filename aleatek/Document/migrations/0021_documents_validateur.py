# Generated by Django 4.2 on 2023-05-28 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Document', '0020_alter_documents_codification_alter_documents_exam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='validateur',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
