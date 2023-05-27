from django.db import models


# Create your models here.

class SERVICES(models.Model):
    code_services = models.IntegerField()
    nom_services = models.CharField(max_length=500)
    implantation = models.CharField(max_length=200)
    pays = models.CharField(max_length=500, default='France')

    def __str__(self):
        return str(self.code_services)
