# Generated by Django 4.2 on 2023-05-24 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Document', '0009_alter_documents_numero_aleatek_affectationdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affectationdocument',
            name='affecte_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affectations', to=settings.AUTH_USER_MODEL),
        ),
    ]
