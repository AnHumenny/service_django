INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.index.apps.IndexConfig',
    'apps.accident.apps.AccidentConfig',
    'apps.key.apps.KeyConfig',
    'apps.fttx.apps.FttxConfig',
    'apps.manual.apps.ManualConfig',
    'apps.base_station.apps.BaseStationConfig',
    'apps.info.apps.InfoConfig',
    'apps.filewiever.apps.FilewieverConfig',
    'apps.gazprom.apps.GazpromConfig',
    'apps.analutics.apps.AnaluticsConfig',
    'apps.subtable.apps.SubtableConfig',
    'apps.material.apps.MaterialConfig',
    'apps.user_setting',
    'tinymce',
    'api',
    'rest_framework',
    'apps.google_calendar',
    'drf_spectacular',
    "django_celery_beat",
    "apps.accident_calendar.apps.AccidentCalendarConfig",
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
