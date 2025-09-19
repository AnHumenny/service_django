from django.apps import AppConfig


class AccidentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accident'

    def ready(self):
        import apps.accident_calendar.signals