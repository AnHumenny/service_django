import os

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = os.getenv("CELERY_TIMEZONE")

USE_I18N = True

USE_TZ = True

DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

USE_L10N = False
