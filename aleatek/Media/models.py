from django.db import models

from collaborateurs.models import Collaborateurs


# Create your models here.

class Media(models.Model):
    charg_affaire = models.ForeignKey(Collaborateurs, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, default="name")
    identification = models.CharField(max_length=25)
    complement = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.name
