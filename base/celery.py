import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

app = Celery('service_django')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
from dotenv import load_dotenv

load_dotenv()

def cron_with_offset(offset: int = 0):
    base_hour = int(os.getenv("CRON_HOUR", 0))
    base_minute = int(os.getenv("CRON_MINUTE", 0)) + offset
    hour = (base_hour + (base_minute // 60)) % 24
    minute = base_minute % 60
    return crontab(hour=hour, minute=minute)


app.conf.beat_schedule = {
    "monthly_task_fttx": {
        "task": "info.tasks.csv_actual_month",
         "schedule": cron_with_offset(0),
    },
    "monthly_task_fttx_organization": {
        "task": "info.tasks.monthly_task_fttx_organization",
         "schedule": cron_with_offset(1),
    },
    "daily_task_fttx": {
        "task": "info.tasks.csv_daily_fttx",
         "schedule": cron_with_offset(2),
    },
    "daily_task_fttx_for_organization": {
        "task": "info.tasks.daily_task_fttx_for_organization",
        "schedule": cron_with_offset(3),
    },
    "csv_actual_accident_month": {
        "task": "accident.tasks.csv_actual_accident_month",
         "schedule": cron_with_offset(4),
    },
    "monthly_task_accident_organization": {
        "task": "accident.tasks.monthly_task_accident_organization",
         "schedule": cron_with_offset(5),
    },
    "csv_daily_accident": {
        "task": "accident.tasks.csv_daily_accident",
         "schedule": cron_with_offset(6),
    },
    "daily_accident_for_organization": {
        "task": "accident.tasks.daily_accident_for_organization",
         "schedule": cron_with_offset(7),
    },
}
