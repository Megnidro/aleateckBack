from django.db import models

from constructeurs.models import Entreprise


# Create your models here.

class Ouvrages(models.Model):
    libelle = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle

class EntrepriseAssocieOuvrages(models.Model):
    constructeurs = models.ManyToManyField(Entreprise)
    diffusion_systematique = models.BooleanField(default=False)
    activite = models.CharField(max_length=20)
    libelle_lot = models.CharField(max_length=30)
    type_douvrage = models.CharField(max_length=20)
    types = models.CharField(max_length=20)
    tableau_diffusion = models.ManyToManyField(Entreprise, related_name='entreprisesovrages')



class AvisOuvrages(models.Model):
    ouvrages = models.ForeignKey(Ouvrages, on_delete=models.CASCADE)
    commentaire = models.CharField(max_length=500)
    image = models.ImageField(upload_to='imageOuvrage', default='')

    def __str__(self):
        return self.avis




















class OuvragesDiffusion(models.Model):
    ouvrages_diffusion = models.IntegerField(blank=True, default=1)
    a_risque = models.BooleanField(default=True)
    diffusion_systematique = models.BooleanField(default=False)
    activite = models.CharField(max_length=50)
    ouvrage_type = models.ForeignKey(Ouvrages, on_delete=models.CASCADE)
    code_ged = models.CharField(max_length=5, blank=True)