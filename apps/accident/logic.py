from datetime import timedelta
from django.http import HttpResponse
import csv
from django.utils import timezone
from .models import Accident


def current_csv():
    """скачать отчёт fttx/wttx(инциденты) в csv текущий месяц"""
    now = timezone.now()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="accident.csv"'

    first_day_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_month = (first_day_of_month.replace(month=first_day_of_month.month + 1, day=1) - timezone.timedelta(
        days=1)) if now.month < 12 else now.replace(year=now.year + 1, month=1, day=1) - timezone.timedelta(days=1)

    accidents = list(Accident.objects.filter(datetime_close__range=(first_day_of_month, last_day_of_month))
                     .filter(status="close").order_by("-id"))

    writer = csv.writer(response, delimiter='*')
    writer.writerow(['Номер', 'Категория', 'Дата открытия', 'Проблема', 'Город', 'Адрес', 'ФИО\юрлицо',
                      'Решение'])

    for accident in accidents:
        writer.writerow([
            accident.number,
            accident.category,
            accident.datetime_open.strftime('%Y-%m-%d'),
            accident.problem,
            accident.city,
            accident.address,
            accident.name,
            accident.decide,
        ])
    return response


def previos_csv():
    """скачать отчёт fttx/wttx(инциденты) csv предыдущий месяц"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="accident_previous_month.csv"'
    now = timezone.now()

    first_day_of_current_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_previous_month = first_day_of_current_month - timedelta(seconds=1)
    first_day_of_previous_month = last_day_of_previous_month.replace(day=1)

    accidents = Accident.objects.filter(
        datetime_close__gte=first_day_of_previous_month,
        datetime_close__lte=last_day_of_previous_month,
        status="close"
    ).order_by("id")

    if not accidents.exists():
        response.write("No accidents found for the previous month.")
        return response

    writer = csv.writer(response, delimiter='*')
    writer.writerow(['Номер', 'Категория', 'Дата открытия', 'Проблема', 'Город', 'Адрес', 'ФИО\юрлицо',
                      'Решение'])

    for accident in accidents:
        writer.writerow([
            accident.number,
            accident.category,
            accident.datetime_open.strftime('%Y-%m-%d %H:%M') if accident.datetime_open else '',
            accident.problem,
            accident.city,
            accident.address,
            accident.name,
            accident.decide,
        ])
    return response
