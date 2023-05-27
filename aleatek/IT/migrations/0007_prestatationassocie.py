# Generated by Django 4.2 on 2023-05-23 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0006_delete_interventiontechniques'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrestatationAssocie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_prestations', models.CharField(max_length=5)),
                ('nom_prestation', models.CharField(max_length=20)),
                ('cree_le', models.DateField()),
                ('id_intervention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT.interventiontechniqueassocie')),
            ],
        ),
    ]
