# Generated by Django 4.2 on 2023-05-10 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('IT', '0003_rename_cb_propose_interventiontechnique_num_service_propose_and_more'),
        ('clients', '0003_remove_client_date_of_birth'),
        ('destinations', '0003_alter_destination_client'),
        ('services', '0001_initial'),
        ('missions', '0002_delete_prestaionsmissionssignes_delete_prestations'),
        ('collaborateurs', '0001_initial'),
        ('marques', '0002_alter_agence_description'),
        ('constructeurs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affaires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_affaire', models.CharField(max_length=500)),
                ('statut_affaire', models.CharField(choices=[('Encours', 'Encours'), ('Achevé', 'Achevé'), ('Abandonné', 'Abandonné')], max_length=20)),
                ('numero_offre', models.CharField(max_length=20)),
                ('numero_contrat', models.CharField(blank=True, max_length=8)),
                ('numero_contrat_provisoire', models.CharField(blank=True, max_length=6)),
                ('libelle_contrat', models.CharField(blank=True, max_length=500)),
                ('date_contrat', models.DateField()),
                ('assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Affairesssss', to='collaborateurs.collaborateurs')),
                ('charge_de_affaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Affairesss', to='collaborateurs.collaborateurs')),
                ('chef_projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Affairess', to='collaborateurs.collaborateurs')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Client-RS-ZIG-Ville')),
                ('constructeurs', models.ManyToManyField(to='constructeurs.entreprise')),
                ('intervention_technique', models.ManyToManyField(to='IT.InterventionTechnique')),
                ('marques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marques.agence')),
                ('missions', models.ManyToManyField(to='missions.missions')),
                ('numero_service_en_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
        migrations.CreateModel(
            name='Cloture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daccord', models.BooleanField(default=False, verbose_name='Ok')),
                ('libelle', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DescriptionDuBatiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actions', models.BooleanField(default=False)),
                ('groupes', models.CharField(max_length=500)),
                ('criters', models.CharField(max_length=500)),
                ('descriptions', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='DescriptionSommaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_de_description', models.CharField(max_length=200)),
                ('descriptions', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='InitialisationCreationAffaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.BooleanField(default=False, verbose_name="Nouvelle Affaire et son premier Plan d'affaire")),
                ('plan', models.BooleanField(default=False, verbose_name="Plan d'affaire supplementaire dans affaires courante")),
            ],
        ),
        migrations.CreateModel(
            name='InitiatilisationAnalyseDeRisque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pts_vigilance_et_risque_associe', models.CharField(max_length=1500)),
                ('risque', models.CharField(blank=True, choices=[('Particulier', 'Particulier'), ('Normal', 'Normal')], max_length=20)),
                ('visites_reunions', models.IntegerField(blank=True, verbose_name='visites/reunions')),
                ('raports_initiaux', models.CharField(blank=True, max_length=500)),
                ('syntheses', models.CharField(blank=True, max_length=500)),
                ('nbre_de_document_a_examiner', models.IntegerField()),
                ('fiche_de_transfert', models.FileField(upload_to='file_tranfer')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_pro', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutore', models.CharField(max_length=500)),
                ('date_de_debut', models.DateField()),
                ('date_de_fin', models.DateField()),
                ('actions', models.BooleanField(default=False)),
                ('accompagnant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.collaborateurs')),
                ('affaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashbord.affaires')),
                ('intervention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT.interventiontechnique')),
            ],
        ),
        migrations.CreateModel(
            name='PlanAffaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_plan_affaire', models.CharField(max_length=500)),
                ('numero_plan', models.IntegerField()),
                ('risque', models.CharField(choices=[], max_length=200)),
                ('devise', models.CharField(choices=[('$', '$'), ('€', '€')], max_length=2)),
                ('debut_chantier', models.DateField(blank=True)),
                ('fin_chantier', models.DateField()),
                ('visite_reunions', models.CharField(blank=True, max_length=10)),
                ('cplt_geo', models.CharField(max_length=250)),
                ('numero_voie', models.CharField(max_length=500)),
                ('lieu_dit', models.CharField(max_length=250)),
                ('compte_postal', models.CharField(max_length=5)),
                ('ville', models.CharField(max_length=500)),
                ('pays', models.CharField(default='France', max_length=500)),
                ('departement', models.CharField(default='Mompellier', max_length=500)),
                ('province', models.CharField(max_length=500)),
                ('type_affaire', models.CharField(choices=[], max_length=500)),
                ('montant_des_travaux', models.IntegerField()),
                ('type_montant', models.CharField(choices=[('HT', 'HT'), ('TTC', 'TTC')], max_length=200)),
                ('debut_prestation_bv', models.DateField()),
                ('nb', models.CharField(max_length=500, verbose_name='Nbre de document à examiner')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.destination')),
                ('numero_affaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashbord.affaires')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashbord.produit')),
            ],
        ),
        migrations.CreateModel(
            name='AdminChargeInteragirAffaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.collaborateurs')),
                ('libelle_it', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT.interventiontechnique')),
                ('secretariat', models.ForeignKey(default='Aucun', on_delete=django.db.models.deletion.CASCADE, related_name='AdminChargeInteragirAffaires', to='collaborateurs.collaborateurs')),
            ],
        ),
    ]
