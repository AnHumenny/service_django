from django.core.paginator import Paginator
from django.shortcuts import render
from .logic import current_csv, previos_csv
from .models import Accident
from django.views.generic import (
    ListView,
    DetailView,
)

class AccidentListView(ListView):
    """Инциденты общий лист"""
    model = Accident
    queryset = Accident.objects.all().order_by("-id")
    paginate_by = 20

class AccidentOpenView(ListView):
    """Инциденты в статусе `Open`"""
    model = Accident
    queryset = Accident.objects.order_by("-id").filter(status="open")[:5]
    paginate_by = 20

class AccidentCloseView(ListView):
    """Инциденты в статусе `Close`"""
    model = Accident
    queryset = Accident.objects.order_by("-id").filter(status="close")[:30]
    paginate_by = 20

class AccidentCheckView(ListView):
    """Инциденты в статусе `Check`"""
    model = Accident
    queryset = Accident.objects.order_by("-id").filter(status="check")
    paginate_by = 20

class AccidentDetailView(DetailView):
    """Инциденты детальный по id"""
    model = Accident


def download_actual_accident(request):
    """скачать отчёт fttx/wttx(инциденты) в csv текущий месяц"""
    return current_csv()

def download_previos_accident(request):
    """скачать отчёт fttx/wttx(инциденты) csv предыдущий месяц"""
    return previos_csv()


def listing(request):
    inc = Accident.objects.all()
    paginator = Paginator(inc, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "accident_list.html", {"page_obj": page_obj, "accident_list": inc})



