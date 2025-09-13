from django.apps import AppConfig

class AccidentCalendarConfig(AppConfig):
    """Configuration for the accident_calendar Django app.

    Defines the app's default auto field and name, and imports signals upon app initialization."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accident_calendar'

    def ready(self):
        import accident_calendar.signals
