# Generated by Django 4.2 on 2023-05-30 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructeurs', '0004_rename_code_postal_pour_envoie_mail_entreprise_code_postal_and_more'),
        ('Dashbord', '0022_remove_planaffaire_intervenant_affaires_intervenant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affaires',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructeurs.entreprise', verbose_name='Client-RS-ZIG-Ville'),
        ),
    ]
