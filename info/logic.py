import csv
from django.utils import timezone
from .forms import DateForm
from .models import Info
from django.http import HttpResponse


def csv_actual_month():
    """скачать отчёт fttx в csv текущий месяц"""
    now = timezone.now()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fttx_actual_month.csv"'
    first_day_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_month = (first_day_of_month.replace(month=first_day_of_month.month + 1, day=1) - timezone.timedelta(
        days=1)) if now.month < 12 else now.replace(year=now.year + 1, month=1, day=1) - timezone.timedelta(days=1)
    writer = csv.writer(response)
    writer.writerow(['ID', 'Реестр', 'Дата', 'Город', 'Улица', 'Дом', 'Квартира',
                     'ФИО абонента', 'кабель 1', 'кабель 2', 'кабель 3', 'коннектор'])
    for obj in Info.objects.all().filter(date_created__range=(first_day_of_month, last_day_of_month)).order_by("id"):
        writer.writerow([obj.id,
                         obj.reestr,
                         obj.date_created.strftime('%Y-%m-%d'),
                         obj.city,
                         obj.street,
                         obj.home,
                         obj.apartment,
                         obj.name,
                         obj.cable_1,
                         obj.cable_2,
                         obj.cable_3,
                         obj.connector
                         ])
    return response


def range_view(request):
    """форма fttx выбрать по датам, скачать в csv"""
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            objects = Info.objects.filter(date_created__range=(start_date, end_date)).order_by("id")
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="select_date_fttx.csv"'
            writer = csv.writer(response)
            writer.writerow(['ID', 'Реестр', 'Дата', 'Город', 'Улица', 'Дом',
                             'ФИО абонента', 'кабель 1', 'кабель 2', 'кабель 3', 'коннектор'])
            for obj in objects:
                writer.writerow([
                    obj.id,
                    obj.reestr,
                    obj.date_created.strftime('%Y-%m-%d'),
                    obj.city,
                    obj.street,
                    obj.home,
                    obj.apartment,
                    obj.name,
                    obj.cable_1,
                    obj.cable_2,
                    obj.cable_3,
                    obj.connector,
                ])
            if not objects:
                writer.writerow(['Нет данных за указанный период'])
            return response
        else:
            return {"form": form, "error": "Пожалуйста, исправьте ошибки в форме."}
    else:
        form = DateForm()
        return {"form": form}
