from django.contrib import admin
from .models import AIE, RapportConception, StatutSaisiRapport, RapportDeVisite

# Register your models here.
admin.site.register(AIE)
admin.site.register(RapportConception)


class SatatuRapportAdmin(admin.ModelAdmin):
    list_display = ['saisie', 'libelle']


admin.site.register(StatutSaisiRapport, SatatuRapportAdmin)
admin.site.register(RapportDeVisite)

