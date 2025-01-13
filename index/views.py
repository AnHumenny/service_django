from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from info.models import Info
from accident.models import Accident
from .models import Index, Material, ExpansionFttx
from fttx.models import Fttx
from key.models import Key
from manual.models import Manual
from datetime import date
from django.views.generic import (
    ListView,
    DetailView,
)

class IndexListView(ListView):
    model = Index
    paginate_by = 3

class IndexDetailView(DetailView):
    model = Index

class InfoDataView(ListView):
    model = Info

now = date.today()

def start_page(request):
    start_date = timezone.datetime(now.year, 1, 1)
    end_date = timezone.datetime(now.year, 12, 31)
    ind = Index.objects.order_by("-id")[:30]  # 30 последних записей
    paginator = Paginator(ind, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data_obj = (Info.objects.filter(date_created__range=(start_date, end_date)).order_by("-id").
                values("id", "reestr", "date_created", "city", "street", "home", "apartment", "name", ))
    paginator = Paginator(data_obj, 10)
    page_number = request.GET.get("pag")
    data = paginator.get_page(page_number)
    result_cable = Info.objects.values("street").filter(date_created__range=(start_date, end_date)).annotate(
          month=TruncMonth('date_created')).values('city', 'month').annotate(total_amount=Sum('cable_1')+Sum('cable_2')+Sum("cable_3")).order_by('month')
    current_year = datetime.now().year

    result_expansion = (
        ExpansionFttx.objects
        .filter(date__year=current_year)  # Фильтруем по году
        .aggregate(total_cable=Sum('cable'))  # Суммируем все значения поля `cable`
    )
    print(f"Общая сумма всех значений cable за {current_year} год: {result_expansion['total_cable']}")
    res_expansion = result_expansion['total_cable']

    print(current_year)
    result_year = Material.objects.values_list('cable', flat=True).first()
    print("result_cable", result_cable)
    total_sum = result_cable.aggregate(total_sum=Sum('total_amount'))['total_sum']
    print("total_sum", total_sum)
    print("result_year" , result_year)
    if result_year is None or total_sum is None:
        total = None
    else:
        total = result_year - total_sum - res_expansion

    l = (Info.objects.filter(date_created__range=(start_date, end_date))
         .annotate(month=TruncMonth('date_created'))
         .values('month')
         .annotate(count=Count('id')).order_by('month')
         )
    dat = []
    for row in l:
        temp = row.get("count")
        dat.append(int(temp))
    accident_query = Accident.objects.order_by("-id").filter(status="open")
    paginator = Paginator(accident_query, 10)
    page_number = request.GET.get("pag")
    accident = paginator.get_page(page_number)
    check_query = Accident.objects.order_by("-id").filter(status="check")
    paginator = Paginator(check_query, 10)  # Show 25  per page.
    page_number = request.GET.get("pag")
    check = paginator.get_page(page_number)
    close_query = Accident.objects.order_by("-id").filter(status="close")[:10]
    paginator = Paginator(close_query, 10)
    page_number = request.GET.get("pag")
    close = paginator.get_page(page_number)
    return render(request, "index/index_list.html", {"page_obj": page_obj, "result_cable": result_cable, "data_list": data,
                                                     "date": dat, "accident": accident, "check": check, "close": close,
                                                    "total": total, "current_year" : current_year, "res_expansion": res_expansion})

def search(request):
    result = request.GET.get('q')
    query = result.split(", ")
    if len(query) < 2 or len(query) > 30 :
        return render(request, 'index/search_results.html',
                      {'uncorrect': "Некорректные условия запроса! "})
    if query[0] == "старт":
        results = Index.objects.all()
        if query[1]:
            results = results.filter(content__icontains=query[1])
            return render(request, 'index/search_results.html', {'uncorrect': results})
    if query[0] == "инфо":
        results = Info.objects.all()
        if query[1]:
            info_list = results.filter(name__icontains=query[1])
            return render(request, 'info/info_list.html', {'info_list': info_list})
    if query[0] == "инцидент":
        results = Accident.objects.all()
        if query[1]:
            accident_name = results.filter(name__icontains=query[1]).order_by("id")
            return render(request, 'accident/accident_list.html', {'accident_list': accident_name})
    if query[0] == "мануал":
        results = Manual.objects.all()
        if query[1]:
            manual = results.filter(type=query[1])
            return render(request, 'manual/manual_list.html', {'manual_list': manual})
    if query[0] == "fttx":
        fttx_search = get_object_or_404(Fttx, city=query[1], street=query[2], number=query[3])
        return render(request, 'fttx/fttx_detail.html', {'fttx': fttx_search})
    if query[0] == "ключ":
        key_search = get_object_or_404(Key, city=query[1], street=query[2], home=query[3])
        return render(request, 'key/key_detail.html', {'key': key_search})