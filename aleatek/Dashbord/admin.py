from django.contrib import admin
from .models import PlanAffaire, Produit, Affaires, \
    InitialisationCreationAffaire

# Register your models here.
#admin.site.register(InitialisationCreationAffaire)
admin.site.register(PlanAffaire)
admin.site.register(Produit)
admin.site.register(Affaires)









