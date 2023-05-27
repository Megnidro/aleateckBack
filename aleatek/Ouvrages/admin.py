from django.contrib import admin
from .models import Ouvrages, AvisOuvrages, OuvragesDiffusion
# Register your models here.
admin.site.register(Ouvrages)
admin.site.register(AvisOuvrages)
admin.site.register(OuvragesDiffusion)