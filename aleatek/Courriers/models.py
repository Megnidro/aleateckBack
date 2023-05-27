from django.db import models

from IT.models import InterventionTechniqueAssocie

from Aso.models import ASO

# Create your models here.
CATEGORY = [
    ('Technique', 'Technique'),
    ('Administratif', 'Administratif')
]


class Courriers(models.Model):
    nume_courrier = models.CharField(max_length=250, verbose_name="Courrier N°")
    category = models.CharField(max_length=20, choices=CATEGORY)
    date_emission = models.DateField()
    aso = models.ForeignKey(ASO, on_delete=models.CASCADE)
    objet = models.CharField(max_length=500)
    intervention_techiniques = models.ManyToManyField(InterventionTechniqueAssocie)
    a_suivre = models.BooleanField(default=True)

    def __str__(self):
        return self.objet
