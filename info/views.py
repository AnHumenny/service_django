from django.shortcuts import render

from index.views import mask_surname
from .logic import  range_view
from .models import Info
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
)


class InfoListView(ListView):
    """список абонов"""
    model = Info
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for obj in context['object_list']:
            obj.name = mask_surname(obj.name)
        return context


class InfoDetailView(DetailView):
    model = Info


def date_range_view(request):
    """форма fttx выбрать по датам, скачать в csv"""
    result = range_view(request)
    if isinstance(result, HttpResponse):
        return result
    return render(request, 'info/csv.html', result)
