import random

from django.db import models

from Ouvrages.models import Ouvrages

from constructeurs.models import Entreprise

from IT.models import InterventionTechniqueAssocie

from Dashbord.models import Affaires

from collaborateurs.models import Collaborateurs


# Create your models here.
class FichierAttache(models.Model):
    prioritaire = models.BooleanField(default=False)
    nom_fichier = models.CharField(max_length=250)
    fichier = models.FileField(upload_to='fichierattachedocument')
    cree_le = models.DateField()
    action = models.BooleanField(default=False)

    def __str__(self):
        return self.nom_fichier



class IntervenantInterventionDocument(models.Model):
    intervenant = models.ManyToManyField(Collaborateurs)
    intervention_technique = models.ManyToManyField(InterventionTechniqueAssocie)
    affecte_le =  models.DateField()
    action = models.BooleanField(default=False)
    affecte_par = models.ForeignKey(Collaborateurs, on_delete=models.CASCADE, related_name='IntervenantInterventionDocuments')

    def __str__(self):
        return self.action




class Avis(models.Model):
    AVIS = [
        ('F', 'F'),
        ('RMQ', 'RMQ'),
        ('FA', 'FA'),
        ('HM', 'HM'),
        ('SO', 'SO'),
        ('VI', 'VI')
    ]
    avis = models.CharField(choices=AVIS, max_length=20)
    commentaire = models.TextField(max_length=500)
    a_suivre = models.BooleanField(default=False)
    collaborateurs = models.ForeignKey(Collaborateurs, on_delete=models.CASCADE, default='')
    valide = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.avis == 'RMQ':
            self.a_suivre = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.avis


"""
    def savef(self, *args, **kwargs):
        if not self.num_avis:
            self.num_avis = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)
"""
class Documents(models.Model):
    emetteur = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='Documentss')
    dossier = models.CharField(max_length=200, default='Execution', choices=(('Execution', 'Execution'), ('Concdption', 'Conception')))
    ouvrage = models.ForeignKey(Ouvrages, on_delete=models.CASCADE, related_name='Documents')
    exam = models.ManyToManyField(Avis)
    nature = models.CharField(max_length=20, default='Plan')
    numero_externe = models.IntegerField(verbose_name='N° Externe')
    numero_aleatek = models.ForeignKey(Affaires, on_delete=models.CASCADE)
    date_de_indice = models.DateField()
    date_de_reception = models.DateField()
    indice = models.CharField(max_length=5)
    titre = models.CharField(max_length=500)
    num_revision = models.CharField(max_length=20, verbose_name='N° révision', default=1)
    fichier_attache = models.ManyToManyField(FichierAttache, blank=True)
    affectation = models.ManyToManyField(IntervenantInterventionDocument)

    def __str__(self):
        return self.titre
