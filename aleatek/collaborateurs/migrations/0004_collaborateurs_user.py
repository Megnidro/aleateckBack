# Generated by Django 4.2 on 2023-05-23 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collaborateurs', '0003_alter_collaborateurs_numero_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborateurs',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]