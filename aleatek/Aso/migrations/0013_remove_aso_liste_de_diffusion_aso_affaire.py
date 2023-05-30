# Generated by Django 4.2 on 2023-05-30 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashbord', '0022_remove_planaffaire_intervenant_affaires_intervenant'),
        ('Aso', '0012_remove_aso_armoire_remove_aso_aso_num_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aso',
            name='liste_de_diffusion',
        ),
        migrations.AddField(
            model_name='aso',
            name='affaire',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Dashbord.affaires'),
            preserve_default=False,
        ),
    ]