from django.db import models


# Create your models here.


class Missions(models.Model):
    code_mission = models.CharField(max_length=3)
    libelle_mission = models.CharField(max_length=35)
    cree_le = models.DateField()

    def __str__(self):
        return self.code_mission

    class Meta:
        verbose_name = 'Mission'
