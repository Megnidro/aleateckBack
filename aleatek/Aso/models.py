import random

from django.db import models

from Ouvrages.models import Ouvrages

from Ouvrages.models import AvisOuvrages

from constructeurs.models import Entreprise

from Document.models import Documents

from collaborateurs.models import Collaborateurs


class ASO(models.Model):
    ETAPES = [
        (0, 'En cours'),
        (1, 'Accepté'),
        (2, 'Classé'),
        (4, 'diffusé')
    ]
    date = models.DateField(null=True)
    ouvrage = models.ForeignKey(Ouvrages, on_delete=models.CASCADE, null=True)
    statut = models.CharField(choices=ETAPES, max_length=50, default=0)
    liste_de_diffusion = models.ManyToManyField(Entreprise)
    redacteur = models.ForeignKey(Collaborateurs, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = "ASO"
        # verbose_name_plural = "ASOS"


""" def save(self, *args, **kwargs):
        if not self.aso_num:
            self.aso_num = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)
   def __str__(self):
        return self.aso_num
"""



class SyntheseAvis(models.Model):
    statut = models.CharField(max_length=10)
    remarque = models.CharField(max_length=100)
    reformuler = models.CharField(max_length=100)
    exprimer_sur = models.CharField(max_length=100)
    objet_du_controle = models.CharField(max_length=100)
    phase = models.CharField(max_length=100)
    verificateur = models.CharField(max_length=100)
    ouvrages = models.CharField(max_length=100)
    photo = models.ImageField()
