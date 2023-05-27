from django.db import models


# Create your models here.


class InterventionTechniqueAssocie(models.Model):
    cod_it = models.CharField(max_length=10)
    libelle_it = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle_it


class PrestatationAssocie(models.Model):
    id_intervention = models.ForeignKey(InterventionTechniqueAssocie, on_delete=models.CASCADE)
    code_prestations = models.CharField(max_length=5)
    nom_prestation = models.CharField(max_length=20)
    cree_le = models.DateField()

    def __str__(self):
        return self.code_prestations


