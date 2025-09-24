from django.core.mail import send_mail
from decouple import config
import calendar
import csv
import io
import os
from datetime import date
from django.core.mail import EmailMessage
from django.utils import timezone
from apps.accident.models import Accident
from apps.info.models import Info
from celery import shared_task
from apps.subtable.models import SubOrganization

accident_report = os.getenv("ACCIDENT_REPORT")

@shared_task
def send_accident_email(accident_id, email_data):
    """Send email asynchronously."""
    try:
        send_mail(
            subject=email_data['subject'],
            message=email_data['message'],
            from_email=config('EMAIL_HOST_USER'),
            recipient_list=[email_data['recipient']],
            fail_silently=False,
        )
        return f"Email sent for accident {accident_id}"
    except Exception as e:
        return f"Failed to send email for accident {accident_id}: {str(e)}"


@shared_task
def csv_actual_accident_month():
    """Сформировать CSV-отчёт по всем данным за текущий месяц и отправить на указанный email"""
    today = date.today()
    last_day = calendar.monthrange(today.year, today.month)[1]

    if today.day != last_day:
        return "Сегодня не последний день месяца, задача пропущена"

    now = timezone.now()
    first_day_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_month = (
        first_day_of_month.replace(month=first_day_of_month.month % 12 + 1, day=1)
        - timezone.timedelta(days=1)
    )
    if first_day_of_month.month == 12:
        last_day_of_month = last_day_of_month.replace(year=last_day_of_month.year + 1)

    output = io.StringIO()
    writer = csv.writer(output)
    headers = os.getenv("CSV_HEADERS_FTTX", "").split(",")
    writer.writerow(headers)

    query = Accident.objects.filter(date_created__range=(first_day_of_month, last_day_of_month)).order_by("id")
    for obj in query.iterator():
        writer.writerow([
            obj.id,
            obj.number,
            obj.category,
            obj.sla,
            obj.datetime_open.strftime('%Y-%m-%d'),
            obj.datetime_close.strftime('%Y-%m-%d'),
            obj.problem,
            obj.city,
            obj.address,
            obj.name,
            obj.phone,
            obj.subscriber,
            obj.comment,
            obj.decide,
            obj.organization,
            obj.status,
        ])

    csv_content = output.getvalue()
    output.close()

    email = EmailMessage(
        subject="Отчёт по инцидентам за текущий месяц",
        body="Во вложении отчёт в формате CSV.",
        from_email=f"{accident_report}",
        to=[os.getenv("EMAIL_HOST_USER")],
    )
    email.attach(f"отчёт_{today}.csv", csv_content, "text/csv")
    email.send()

    return f"Отчёт отправлен на {os.getenv("EMAIL_HOST_USER")}"


@shared_task
def monthly_task_accident_organization():
    """Сформировать CSV-отчёт за текущий месяц и отправить каждой организации отдельно"""
    today = date.today()
    last_day = calendar.monthrange(today.year, today.month)[1]

    if today.day != last_day:
        return "Сегодня не последний день месяца, задача пропущена"

    now = timezone.now()
    first_day_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_month = now.replace(day=last_day, hour=23, minute=59, second=59, microsecond=999999)

    for org in SubOrganization.objects.all():
        output = io.StringIO()
        writer = csv.writer(output)
        headers = os.getenv("CSV_HEADERS_FTTX", "").split(",")
        writer.writerow(headers)

        query = Info.objects.filter(
            date_created__range=(first_day_of_month, last_day_of_month),
            organization=org
        ).order_by("id")

        if not query.exists():
            continue

        for obj in query.iterator():
            writer.writerow([
                obj.id,
                obj.number,
                obj.category,
                obj.sla,
                obj.datetime_open.strftime('%Y-%m-%d'),
                obj.datetime_close.strftime('%Y-%m-%d'),
                obj.problem,
                obj.city,
                obj.address,
                obj.name,
                obj.phone,
                obj.subscriber,
                obj.comment,
                obj.decide,
                obj.organization,
                obj.status,
            ])

        csv_content = output.getvalue()
        output.close()

        email = EmailMessage(
            subject=f"Отчёт FTTX за {now.strftime('%B %Y')} — {org.name}",
            body="Во вложении отчёт в формате CSV.",
            from_email=f"{accident_report}",
            to=[org.email],
        )
        email.attach(f"отчёт_{today}_{org.name}.csv", csv_content, "text/csv")
        email.send()

    return f"Отчёты отправлены {SubOrganization.objects.count()} организациям"


@shared_task
def csv_daily_accident():
    """Сформировать CSV-отчёт за текущий день и отправить суперадмину."""
    superadmin_email = os.getenv("EMAIL_HOST_USER")
    now = timezone.now()

    start_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)

    output = io.StringIO()
    writer = csv.writer(output)
    headers = os.getenv("CSV_HEADERS_FTTX", "").split(",")
    writer.writerow(headers)

    query = Info.objects.filter(date_created__range=(start_day, end_day)).order_by("id")
    for obj in query.iterator():
        writer.writerow([
            obj.id,
            obj.number,
            obj.category,
            obj.sla,
            obj.datetime_open.strftime('%Y-%m-%d') if obj.datetime_open else "",
            obj.datetime_close.strftime('%Y-%m-%d') if obj.datetime_close else "",
            obj.problem,
            obj.city,
            obj.address,
            obj.name,
            obj.phone,
            obj.subscriber,
            obj.comment,
            obj.decide,
            obj.organization,
            obj.status,
        ])

    csv_content = output.getvalue()
    output.close()

    email = EmailMessage(
        subject=f"Отчёт FTTX (аварии) за {now.strftime('%d.%m.%Y')}",
        body="Во вложении отчёт в формате CSV.",
        from_email=f"{accident_report}",
        to=[superadmin_email],
    )
    email.attach(f"отчёт_аварии_{now.strftime('%Y-%m-%d')}.csv", csv_content, "text/csv")
    email.send()

    return f"Отчёт отправлен на {superadmin_email}"


@shared_task
def daily_accident_for_organization():
    """
    Сформировать CSV-отчёт за текущий день для каждой организации
    и отправить на email организации.
    """
    now = timezone.now()
    start_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)

    for org in SubOrganization.objects.all():
        output = io.StringIO()
        writer = csv.writer(output)
        headers = os.getenv("CSV_HEADERS_FTTX", "").split(",")
        writer.writerow(headers)

        query = Info.objects.filter(
            organization=org,
            date_created__range=(start_day, end_day)
        ).order_by("id")

        if not query.exists():
            continue

        for obj in query.iterator():
            writer.writerow([
                obj.id,
                obj.number,
                obj.category,
                obj.sla,
                obj.datetime_open.strftime('%Y-%m-%d') if obj.datetime_open else "",
                obj.datetime_close.strftime('%Y-%m-%d') if obj.datetime_close else "",
                obj.problem,
                obj.city,
                obj.address,
                obj.name,
                obj.phone,
                obj.subscriber,
                obj.comment,
                obj.decide,
                obj.organization,
                obj.status,
            ])

        csv_content = output.getvalue()
        output.close()

        if org.email:
            email = EmailMessage(
                subject=f"Отчёт FTTX (аварии) за {now.strftime('%d.%m.%Y')} для {org.name}",
                body="Во вложении отчёт в формате CSV.",
                from_email=f"{accident_report}",
                to=[org.email],
            )
            email.attach(f"отчёт_аварии_{org.name}_{now.strftime('%Y-%m-%d')}.csv",
                         csv_content, "text/csv")
            email.send()

    return "Отчёты отправлены всем организациям"
