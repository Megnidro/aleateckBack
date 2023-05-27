import random

from django.db import models

from Ouvrages.models import Ouvrages

from Ouvrages.models import AvisOuvrages

from constructeurs.models import Entreprise

from Document.models import Documents


class ASO(models.Model):
    ETAPES = [
        ('En cours de saisi', 'En cours de saisi'),
        ('Accepté', 'Accepté'),
        ('Classé', 'Classé'),
        ('Préparé', 'Préparé')
    ]
    aso_num = models.IntegerField(verbose_name='ASO N°', blank=True)
    date = models.DateField(null=True)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    nos_reference = models.CharField(max_length=500)
    avis_ouvrage = models.ForeignKey(AvisOuvrages, on_delete=models.CASCADE, null=True, )
    balise_a_solder = models.CharField(max_length=500)
    etape = models.CharField(choices=ETAPES, max_length=50)
    imprime = models.BooleanField(default=False)
    mel = models.BooleanField(default=False)
    fax = models.BooleanField(default=False)
    edossier = models.BooleanField(default=False)
    armoire = models.BooleanField(default=False)
    maestro = models.BooleanField(default=False)
    liste_de_diffusion = models.ManyToManyField(Entreprise)

    def save(self, *args, **kwargs):
        if not self.aso_num:
            self.aso_num = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.aso_num

    class Meta:
        verbose_name = "ASO"
        # verbose_name_plural = "ASOS"


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
