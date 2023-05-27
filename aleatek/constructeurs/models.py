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
    raison_social = models.CharField(max_length=20, blank=True)
    numero_siret = models.CharField(max_length=14, blank=True)
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE, blank=True)
    email = models.EmailField()
    code_chantier = models.CharField(max_length=10, blank=True)
    # media_diffusion = models.CharField(choices=DIFFUSION, max_length=15)
    mel = models.BooleanField(default=True)
    fax = models.BooleanField(default=False)
    courrier = models.BooleanField(default=False)
    code_postal_pour_envoie_mail = models.BooleanField(default=False, blank=True)
    boite_postal = models.CharField(max_length=5, blank=True)
    bureau_distributeur = models.CharField(max_length=20)
    cedex = models.CharField(max_length=20)
    cplt_geo = models.CharField(max_length=20)
    numero_voie = models.CharField(max_length=10, blank=True, verbose_name='N° et Voie')
    lieu_dit = models.CharField(max_length=20)
    cp = models.CharField(max_length=15)
    ville = models.CharField(max_length=20)
    departement = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
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
