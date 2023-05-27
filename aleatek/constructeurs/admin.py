from django.contrib import admin

# Register your models here.
from .models import Entreprise, Activite, MediaCommunications


class MadiaAdminModel(admin.ModelAdmin):
    list_display = ['media', 'identification', 'complement']


class EntrepriseAdminModel(admin.ModelAdmin):
    list_display = ['raison_social', 'mel', 'cedex', 'courrier']


admin.site.register(Activite)
admin.site.register(Entreprise, EntrepriseAdminModel)

admin.site.register(MediaCommunications, MadiaAdminModel)
