# Generated by Django 4.2 on 2023-04-18 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborateurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilite', models.CharField(choices=[('Mlle', 'Mlle'), ('M', 'M'), ('Mme', 'Mme')], max_length=10)),
                ('nom', models.CharField(max_length=500)),
                ('prenom', models.CharField(max_length=500, verbose_name='Prénoms')),
                ('implantation', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
                ('numero_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
    ]