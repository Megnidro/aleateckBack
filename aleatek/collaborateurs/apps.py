from django.apps import AppConfig


class CollaborateursConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'collaborateurs'

    def ready(self):
        import collaborateurs.signals  # Ajoutez cette ligne

