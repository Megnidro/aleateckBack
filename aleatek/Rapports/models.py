from django.db import models
from ckeditor.fields import RichTextField
from missions.models import Missions

from IT.models import InterventionTechniqueAssocie

from destinations.models import Destination

from Dashbord.models import Affaires

from Ouvrages.models import Ouvrages


class StatutSaisiRapport(models.Model):
    STATUTS = [
        ('RICT', 'RICT'),
        ('RIAOERP', 'RIAOERP'),
        ('RIAOERT', 'RIAOERT'),
        ('RIAOIGH', 'RIAOIGH'),
        ('PreRapSi', 'PreRapSi'),
        ('RVRAT', 'RVRAT'),
        ('RVMD', 'RVMD'),
        ('Revue', 'Revue'),
    ]

    saisie = models.CharField(max_length=20, choices=STATUTS)
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.saisie} {self.libelle}"


class AIE(models.Model):
    STATUS = [
        ('En cours', 'En cours'),
        ('Classé', 'Classé')
    ]
    numero_aie = models.CharField(max_length=200)
    date_aie = models.DateField()
    periode_phase = models.ForeignKey(StatutSaisiRapport, on_delete=models.CASCADE)
    titre = models.CharField(max_length=500)
    complement = models.CharField(max_length=500, verbose_name='Complement du titre/ ouvrages')
    statut = models.CharField(choices=STATUS, max_length=500)
    redacteur = models.CharField(max_length=500)
    date_de_diffusion = models.DateField()
    etat_aie = models.CharField(max_length=500)
    redactions = models.FileField(upload_to='Redaction Aie')

    def __str__(self):
        return self.titre


class RapportConception(models.Model):
    phase = models.ManyToManyField(StatutSaisiRapport, verbose_name='PhaseCode')
    titre = models.ForeignKey(AIE, on_delete=models.CASCADE, default="")
    complement_titre = models.ForeignKey(AIE, on_delete=models.CASCADE, default="", related_name='RapportConceptions')
    missions = models.ManyToManyField(Missions)
    interventions_associe = models.ManyToManyField(InterventionTechniqueAssocie)
    description_batiment = models.ManyToManyField(Destination)

    def __str__(self):
        return self.phase

class RapportDeVisite(models.Model):
    affaire = models.ForeignKey(Affaires, on_delete=models.CASCADE)
    ouvrage = models.ForeignKey(Ouvrages, on_delete=models.CASCADE, default="")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, default="")
    objet = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True, verbose_name='contenu')

    def __str__(self):
        return self.objet
