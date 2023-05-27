# Generated by Django 4.2 on 2023-05-20 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaborateurs', '0002_alter_collaborateurs_address_and_more'),
        ('destinations', '0006_remove_destination_batiment_and_more'),
        ('Rapports', '0004_alter_rapportconception_description_batiment'),
        ('Dashbord', '0013_alter_planaffaire_affaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminchargeinteragiraffaire',
            name='chef_projet',
        ),
        migrations.RemoveField(
            model_name='adminchargeinteragiraffaire',
            name='libelle_it',
        ),
        migrations.RemoveField(
            model_name='adminchargeinteragiraffaire',
            name='secretariat',
        ),
        migrations.DeleteModel(
            name='Cloture',
        ),
        migrations.DeleteModel(
            name='DescriptionSommaire',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='batiment',
        ),
        migrations.DeleteModel(
            name='InitiatilisationAnalyseDeRisque',
        ),
        migrations.RemoveField(
            model_name='tutorat',
            name='accompagnant',
        ),
        migrations.RemoveField(
            model_name='tutorat',
            name='affaire',
        ),
        migrations.RemoveField(
            model_name='tutorat',
            name='intervention',
        ),
        migrations.AddField(
            model_name='planaffaire',
            name='tutorat',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.collaborateurs'),
        ),
        migrations.AlterField(
            model_name='initialisationcreationaffaire',
            name='creation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashbord.affaires'),
        ),
        migrations.AlterField(
            model_name='initialisationcreationaffaire',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashbord.planaffaire'),
        ),
        migrations.AlterField(
            model_name='planaffaire',
            name='affaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planaffaires', to='Dashbord.affaires'),
        ),
        migrations.RemoveField(
            model_name='planaffaire',
            name='destination',
        ),
        migrations.DeleteModel(
            name='AdminChargeInteragirAffaire',
        ),
        migrations.DeleteModel(
            name='DescriptionDuBatiment',
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
        migrations.DeleteModel(
            name='Tutorat',
        ),
        migrations.AddField(
            model_name='planaffaire',
            name='destination',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='destinations.destination'),
        ),
    ]