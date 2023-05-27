from django.db import models

from constructeurs.models import Entreprise


# Create your models here.

class Ouvrages(models.Model):
    libelle = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle


class AvisOuvrages(models.Model):
    ouvrages = models.ForeignKey(Ouvrages, on_delete=models.CASCADE)
    commentaire = models.CharField(max_length=500)

    def __str__(self):
        return self.avis


class OuvragesDiffusion(models.Model):
    designation = models.ForeignKey(Ouvrages, on_delete=models.CASCADE)
    diffusion_systematique = models.BooleanField(default=False)
    activite = models.CharField(max_length=500)
    libelle = models.CharField(max_length=500, verbose_name='Libelle du lot/chantier')
