from datetime import datetime
from django.shortcuts import render, get_object_or_404
from info.models import Info
from accident.models import Accident
from .models import Index
from fttx.models import Fttx
from key.models import Key
from manual.models import Manual
from datetime import date
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .logic import ind, data_obj, all_cable, total_cable, result_exp, res_expansion_wttx, total_utp, accident_query, \
    check_query, close_query, expire


class IndexListView(ListView):
    model = Index
    paginate_by = 3

class IndexDetailView(DetailView):
    model = Index

class InfoDataView(ListView):
    model = Info

now = date.today()

def start_page(request):
    current_year = datetime.now().year
    current_date = datetime.now().strftime("%Y-%m-%d")
    index = ind()
    paginator = Paginator(index, per_page=3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data_object = data_obj()
    paginator = Paginator(data_object, 10)
    page_number = request.GET.get("pag")
    data = paginator.get_page(page_number)

    result_cable = all_cable()
    total_cable_sum = total_cable()
    result_expansion = result_exp()
    result_expansion_wttx = res_expansion_wttx()
    total_sum = total_utp()

    if total_sum is None:
        total = 0
    else:
        total = total_sum - total_cable_sum - result_expansion - result_expansion_wttx

    sum_month = expire()
    accident_q = accident_query()
    paginator = Paginator(accident_q, 10)
    page_number = request.GET.get("pag")
    accident = paginator.get_page(page_number)

    check_q = check_query()
    paginator = Paginator(check_q, 10)
    page_number = request.GET.get("pag")
    check = paginator.get_page(page_number)

    close_q = close_query()
    paginator = Paginator(close_q, 10)
    page_number = request.GET.get("pag")
    close = paginator.get_page(page_number)

    return render(request, "index/index_list.html", {"page_obj": page_obj,  "date": sum_month,
                                                     "result_cable": result_cable, "data_list": data,
                                                     "accident": accident, "check": check, "close": close,
                                                    "total": total, "current_year" : current_year,
                                                     'current_date': current_date,"res_expansion": result_expansion,
                                                     "res_expansion_wttx": result_expansion_wttx})

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