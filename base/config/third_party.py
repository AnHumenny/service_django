import os

TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/3r1qfnyory13br9dbawy1fqparoiltfh8lxl9z2kbsf9c8xn/tinymce/5/tinymce.min.js'
TINYMCE_COMPRESSOR = False

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_OAUTH_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://127.0.0.1:8000/google_calendar/callback/")
GOOGLE_OAUTH_TOKEN_URL = os.getenv("GOOGLE_OAUTH_TOKEN_URL", "https://oauth2.googleapis.com/token")

LOGIN_REDIRECT_URL = '/admin/accident/'
