import csv
from .forms import DateForm
from .models import Info
from django.http import HttpResponse


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
