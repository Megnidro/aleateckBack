from django.contrib import admin

# Register your models here.
from .models import Missions


class MissionAdminModel(admin.ModelAdmin):
    list_display = ('code_mission', 'libelle_mission', 'cree_le')


admin.site.register(Missions, MissionAdminModel)
