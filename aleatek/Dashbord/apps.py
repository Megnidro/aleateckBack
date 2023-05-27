from django.apps import AppConfig


class DashbordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Dashbord'
    verbose_name = "Tableau de Bord"
    ordering = 1

    def ready(self):
        import Dashbord.signals