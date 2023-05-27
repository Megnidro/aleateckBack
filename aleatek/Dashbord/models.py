import random

from django.db import models

from collaborateurs.models import Collaborateurs

from IT.models import InterventionTechniqueAssocie

from clients.models import Client

from services.models import SERVICES

from marques.models import Agence

from missions.models import Missions

from constructeurs.models import Entreprise

from destinations.models import Destination


class Produit(models.Model):
    cod_pro = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Affaires(models.Model):
    AFFAIRES = [
        ('Encours', 'Encours'),
        ('Achevé', 'Achevé'),
        ('Abandonné', 'Abandonné')
    ]
    numero_affaire = models.CharField(max_length=5)
    libelle_affaire = models.CharField(max_length=500)
    statut_affaire = models.CharField(max_length=20, choices=AFFAIRES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client-RS-ZIG-Ville")
    numero_service_en_charge = models.ForeignKey(SERVICES, on_delete=models.CASCADE)
    charge_de_affaire = models.ForeignKey(Collaborateurs, on_delete=models.CASCADE, related_name='Affairesss')
    assistant = models.ForeignKey(Collaborateurs, on_delete=models.CASCADE, related_name='Affairesssss')
    chef_projet = models.ForeignKey(Collaborateurs, on_delete=models.CASCADE, related_name='Affairess')
    marques = models.ForeignKey(Agence, on_delete=models.CASCADE)
    numero_offre = models.CharField(max_length=20)
    numero_contrat = models.CharField(max_length=8, blank=True)
    numero_contrat_provisoire = models.CharField(max_length=6, blank=True)
    libelle_contrat = models.CharField(max_length=500, blank=True)
    date_contrat = models.DateField()
    intervenant = models.ManyToManyField(Collaborateurs)


    def __str__(self):
        return self.libelle_affaire

    def save(self, *args, **kwargs):
        if not self.numero_contrat_provisoire:
            self.numero_contrat_provisoire = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)


class PlanAffaire(models.Model):
    RISQUES = [
        ('Normal', 'Normal'),
        ('Particulier', 'Particulier'),
        ('Complexe', 'Complexe')

    ]
    DEVISE = [
        ('$', '$'),
        ('€', '€')
    ]

    TYPES_AFFAIRES = [
        ('CTC', 'CTC'),
        ('VT', 'VT')

    ]
    affaire = models.ForeignKey(Affaires, on_delete=models.CASCADE, related_name='planaffaires',null=True)
    libelle_plan_affaire = models.CharField(max_length=500)
    numero_plan = models.IntegerField()
    risque = models.CharField(max_length=200, choices=RISQUES)
    devise = models.CharField(max_length=2, choices=DEVISE)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE, default='')
    debut_chantier = models.DateField(blank=True)
    delai_des_travaux = models.CharField(blank=True, help_text='Ce champ se remplie automatiquement')
    fin_chantier = models.DateField()
    visite_reunions = models.CharField(max_length=10, blank=True)
    cplt_geo = models.CharField(max_length=250)
    numero_voie = models.CharField(max_length=500)
    lieu_dit = models.CharField(max_length=250)
    compte_postal = models.CharField(max_length=5, blank=True)
    ville = models.CharField(max_length=500)
    pays = models.CharField(max_length=500, default='France')
    departement = models.CharField(max_length=500, default='Mompellier')
    province = models.CharField(max_length=500)
    type_affaire = models.CharField(max_length=500, choices=TYPES_AFFAIRES)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)
    montant_des_travaux = models.IntegerField()
    type_montant = models.CharField(max_length=200, choices=(
        ('HT', 'HT'), ('TTC', 'TTC')
    ))
    debut_prestation_bv = models.DateField()
    nb = models.CharField(max_length=500, verbose_name='Nbre de document à examiner')
    intervention_technique = models.ManyToManyField(InterventionTechniqueAssocie)
    missions = models.ManyToManyField(Missions)
    constructeurs = models.ManyToManyField(Entreprise)
    tutorat = models.ForeignKey(Collaborateurs, on_delete=models.CASCADE, blank=True, default="", related_name="planaffaires", null=True)

    def delai_des_travaux(self):
        if self.debut_chantier < self.fin_chantier:
            return 'Error, please enter a valide date'
        delta = self.fin_chantier - self.debut_chantier
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)  # {hours}h {minutes}m {seconds}s"
        duration_str = f"{days} jours {hours} heurs {minutes}minutes"
        self.delai_des_travaux = duration_str
        self.save()
        return duration_str

    def __str__(self):
        return self.libelle_plan_affaire


class InitialisationCreationAffaire(models.Model):
    creation = models.ForeignKey(Affaires, on_delete=models.CASCADE)
    plan = models.ForeignKey(PlanAffaire, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.creation)
