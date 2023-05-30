from django.db import models

""" DIFFUSION = [
        ('Mél', 'Mél'),
        ('Fax', 'Fax'),
        ('Courrier', 'Courrier')
    ]
"""


class Activite(models.Model):
    nom = models.CharField(max_length=500)

    def __str__(self):
        return self.nom


class Entreprise(models.Model):
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    raison_social = models.CharField(max_length=20)
    numero_siret = models.CharField(max_length=14)
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20,  blank=True)
    telephone_fixe = models.CharField(max_length=13, blank=True)
    fax = models.CharField(max_length=13, blank=True)
    address = models.CharField(max_length=20, blank=True)
    code_chantier = models.CharField(max_length=10, blank=True)
    code_postal = models.BooleanField(default=False, blank=True)
    numero_voie = models.CharField(max_length=10, blank=True, verbose_name='N° et Voie')
    lieu_dit = models.CharField(max_length=20, blank=True)
    ville = models.CharField(max_length=20, blank=True)
    departement = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20, blank=True)
    pays = models.CharField(max_length=20, default='France')

    def __str__(self):
        return self.raison_social

    class Meta:
        verbose_name = 'Constructeurs'


class MediaCommunications(models.Model):
    media = models.CharField(max_length=500)
    identification = models.CharField(max_length=200)
    complement = models.CharField(max_length=500)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    def __str__(self):
        return self.media
