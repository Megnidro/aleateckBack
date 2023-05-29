from django.contrib import admin

# Register your models here.
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city']
admin.site.register(Client, ClientAdmin)
