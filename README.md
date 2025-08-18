# Django Service Application

Приложение предназначено для обработки и отображения служебной информации (добавление, редактирование, удаление, анализ). Предоставляет API для работы с внешними сервисами, а также использует PostgreSQL в качестве базы данных.


Перед тем как начать, убедитесь, что у вас установлены следующие компоненты:
- **Python** (версия 3.11)
- **PostgreSQL** (версия 14)
- **pip** 
- **virtualenv** (опционально)

## Установка

python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows

## Установите зависимости:
pip install -r requirements.txt

Настройте базу данных:
Создайте базу данных в PostgreSQL и обновите настройки в .env вашего проекта:

    SECRET_KEY='key_django'
    ENGINE='engine'
    DATABASE_PASSWORD='database_password'
    DATABASE_NAME='database_name'
    DATABASE_USER='user'
    DATABASE_HOST='host'
    DATABASE_PORT='port'
    ALLOWED_HOSTS='список ip-адресов'
    TINYMCE_URL='url'
    GOOGLE_CLIENT_ID="client id"
    GOOGLE_CLIENT_SECRET="client secret"
    GOOGLE_OAUTH_TOKEN_URL="https://oauth2.googleapis.com/token"
    GOOGLE_REDIRECT_URI="url redirect callback"
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
    CELERY_TIMEZONE = 'Europe/Minsk'

##Примените миграции:
python manage.py migrate

##Запуск приложения
Чтобы запустить приложение, выполните следующую команду:
python manage.py runserver
