from django.db import models


class Destination(models.Model):
    nom = models.CharField(max_length=50)
    actions = models.BooleanField(default=False)
    groupes = models.CharField(max_length=500, default='')
    criters = models.CharField(max_length=500, default='')
    descriptions = models.CharField(max_length=1500, default='')
    type_de_description = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.nom
