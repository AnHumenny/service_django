INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index.apps.IndexConfig',
    'accident.apps.AccidentConfig',
    'key.apps.KeyConfig',
    'fttx.apps.FttxConfig',
    'manual.apps.ManualConfig',
    'base_station.apps.BaseStationConfig',
    'info.apps.InfoConfig',
    'filewiever.apps.FilewieverConfig',
    'gazprom.apps.GazpromConfig',
    'analutics.apps.AnaluticsConfig',
    'subtable.apps.SubtableConfig',
    'material.apps.MaterialConfig',
    'user_setting',
    'tinymce',
    'api',
    'rest_framework',
    'google_calendar',
    'drf_spectacular',
    "django_celery_beat",
    "accident_calendar.apps.AccidentCalendarConfig",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "My API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "persistAuthorization": True,
    },
    "SECURITY": [{"BearerAuth": []}],
    "COMPONENTS": {
        "securitySchemes": {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            },
        },
    },
}
