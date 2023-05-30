from django.contrib import admin
from .models import FichierAttache, Documents, IntervenantInterventionDocument, Avis
admin.site.register(FichierAttache)


class DocumentAdminVieuw(admin.ModelAdmin):
    list_display = [
        'emetteur', 'dossier', 'ouvrage', 'codification', 'nature', 'numero_aleatek', 'date_de_indice',
        'indice', 'titre'
    ]
admin.site.register(Documents,DocumentAdminVieuw)
admin.site.register(IntervenantInterventionDocument)
admin.site.register(Avis)

