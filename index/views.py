from datetime import datetime
from django.shortcuts import render
from info.models import Info
from .models import Index
from datetime import date
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .logic import ind, data_obj, all_cable, total_cable, result_exp, res_expansion_wttx, total_utp, accident_query, \
    check_query, close_query, expire, info_search, incident_name, incident_addr, man, search_in_fttx, search_in_key, \
    incident_number
import re


class IndexListView(ListView):
    model = Index
    paginate_by = 3

class IndexDetailView(DetailView):
    model = Index

class InfoDataView(ListView):
    model = Info

now = date.today()

def mask_surname(full_name: str) -> str:
    return re.sub(r'^\w+', '***** ', full_name)

def start_page(request):
    current_year = datetime.now().year
    current_date = datetime.now().strftime("%Y-%m-%d")
    index = ind()
    paginator = Paginator(index, per_page=3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data_object = data_obj()

    masked_data = [
        {
            **name,
            'name': mask_surname(name['name'])
        }
        for name in data_object.values()
    ]


    paginator = Paginator(masked_data, 10)
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
    """поиск по параметрам чекбокса"""
    result = request.GET.get('q')
    search_type = request.GET.get('search_type', 'info')
    if len(result) < 2 or len(result) > 30 :
        return render(request, 'index/search_results.html',
                      {'uncorrect': "Некорректные условия запроса! "})

    if search_type == "info":
        info_list = info_search(result)
        if not info_list.exists():
            return render(request, 'info/error.html',
                          {'empty': f"По запросу {result} ничего не найдено"})
        return render(request, 'info/info_list.html', {'info_list': info_list})

    if search_type == "accident_number":
        accident_name = incident_number(result)
        if accident_name is None:
            return render(request, 'accident/error.html',
                          {'empty': f"По запросу {result} ничего не найдено"})
        return render(request, 'accident/accident_list.html', {'accident_list': accident_name})

    if search_type == "accident_name":
        accident_name = incident_name(result)
        if accident_name is None:
            return render(request, 'accident/error.html',
                          {'empty': f"По запросу {result} ничего не найдено"})
        return render(request, 'accident/accident_list.html', {'accident_list': accident_name})

    if search_type == "accident_address":
        accident_addr = incident_addr(result)
        if accident_addr is None:
            return render(request, 'accident/error.html', {'empty': "По запросу ничего не найдено"})
        return render(request, 'accident/accident_list.html', {'accident_list': accident_addr})

    if search_type == "manual":
        manual_query = man(result)
        if manual_query is None:
            return render(request, 'manual/error.html', {'empty': "По запросу ничего не найдено"})
        return render(request, 'manual/manual_list.html', {'manual_list': manual_query})

    if search_type == "fttx":
        fttx_search = search_in_fttx(result)
        if fttx_search is None:
            return render(request, 'fttx/error.html', {'empty': "По запросу ничего не найдено"})
        return render(request, 'fttx/fttx_detail.html', {'fttx': fttx_search})

    if search_type == "key":
        key_search = search_in_key(result)
        if key_search is None:
            return render(request, 'key/error.html', {'empty': "По запросу ничего не найдено"})
        return render(request, 'key/key_detail.html', {'key': key_search})
