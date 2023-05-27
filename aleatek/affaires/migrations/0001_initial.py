# Generated by Django 4.2 on 2023-04-18 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destinations', '0001_initial'),
        ('IT', '0001_initial'),
        ('clients', '0001_initial'),
        ('services', '0001_initial'),
        ('collaborateurs', '0001_initial'),
        ('constructeurs', '0001_initial'),
        ('marques', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanAffaireCreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nvelle', models.BooleanField(default=True, verbose_name="Nouvelle Affaire et son premier plan d'affaire")),
                ('nvelles', models.BooleanField(default=False, verbose_name="Plan d'affaire supplementaire dans Affaire Courante")),
                ('affaire_courante', models.CharField(blank=True, max_length=500)),
                ('numero_contrat', models.CharField(blank=True, max_length=8)),
                ('numero_contrat_provisoire', models.CharField(max_length=6)),
                ('libelle_contrat', models.CharField(blank=True, max_length=500)),
                ('libelle_affaire', models.CharField(blank=True, max_length=500)),
                ('statut_affaire', models.CharField(choices=[('Encours', 'Encours'), ('Achevé', 'Achevé'), ('Abandonné', 'Abandonné')], max_length=20)),
                ('numero_offre', models.CharField(max_length=200)),
                ('date_contrat', models.DateField()),
                ('numero_affaire', models.CharField(max_length=200)),
                ('numero_plan', models.IntegerField(verbose_name='N°Plan')),
                ('libelle_plan_affaire', models.CharField(max_length=500)),
                ('risque', models.CharField(choices=[('Controle Technique', 'Controle Technique'), ('Complexe', 'Complexe'), ('Normative', 'Normative')], max_length=200)),
                ('devise', models.CharField(choices=[('$', '$'), ('€', '€')], max_length=1)),
                ('debut_du_chantier', models.DateField()),
                ('delais_travaux', models.CharField(max_length=200, verbose_name='delai des travaux en Mois')),
                ('fin_du_chantier', models.DateField()),
                ('rapport_inititiaux', models.IntegerField()),
                ('synthese', models.IntegerField()),
                ('visite_reunions', models.IntegerField()),
                ('cplt_geo', models.CharField(max_length=200)),
                ('numero_voie', models.CharField(max_length=20)),
                ('lieu_dit', models.CharField(max_length=500)),
                ('cp', models.CharField(max_length=15)),
                ('ville', models.CharField(max_length=500)),
                ('departement', models.CharField(max_length=500)),
                ('province', models.CharField(max_length=500)),
                ('pays', models.CharField(default='France', max_length=500)),
                ('outil_de_gestion_associe', models.CharField(choices=[('CTC', 'CTC'), ('BAV', 'BAV'), ('CVB', 'SD'), ('Z', 'Z')], max_length=5, verbose_name="Type d'affaire")),
                ('produit', models.CharField(max_length=200)),
                ('montant_des_travaux', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ht', models.CharField(choices=[('HT', 'HT'), ('TTC', 'TTC')], max_length=5)),
                ('type_montant', models.CharField(choices=[('HT', 'HT'), ('TTC', 'TTC')], max_length=3)),
                ('date_debut_prestation_bv', models.DateField()),
                ('nombre_document_examiner', models.IntegerField()),
                ('cb_gestionnaire', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='services.services')),
                ('charge_affaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charge_affaire', to='collaborateurs.collaborateurs')),
                ('chef_de_projet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='chef_de_projet', to='collaborateurs.collaborateurs')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Client(RC-ZIG-Ville')),
                ('destination_ouvrages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.destination')),
                ('libelle_it', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT.it')),
                ('marque', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='marques.agence')),
                ('raison_sociale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructeurs.entreprise')),
                ('secretariat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secretariat', to='collaborateurs.collaborateurs')),
            ],
        ),
    ]