from django.shortcuts import render
from .logic import csv_actual_month, range_view
from .models import Info
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
)


class InfoListView(ListView):
    model = Info
    queryset = Info.objects.all().order_by("-id")
    paginate_by = 50


class InfoDetailView(DetailView):
    model = Info


def download_csv_actual_month(request):
    """скачать отчёт fttx текущий месяц в csv"""
    return csv_actual_month()


def date_range_view(request):
    """форма fttx выбрать по датам, скачать в csv"""
    result = range_view(request)
    if isinstance(result, HttpResponse):
        return result
    return render(request, 'info/csv.html', result)
