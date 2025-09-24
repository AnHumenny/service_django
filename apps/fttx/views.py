from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Fttx

from django.views.generic import (
    ListView,
    DetailView,
)

class FttxListView(ListView):
    """детальная информация по кластерам (весь раздел)"""
    model = Fttx
    queryset = Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")
    paginate_by = 20


class FttxDetailView(DetailView):
    model = Fttx


class FttxClasterMKN16View(ListView):
    model = Fttx
    queryset = (Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")
                .filter(claster="МКН16"))
    paginate_by = 20


class FttxClasterMKN17View(ListView):
    model = Fttx
    queryset = (Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")
                .filter(claster="МКН17"))
    paginate_by = 20


class FttxClasterMKN19View(ListView):
    model = Fttx
    queryset = (Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")
                .filter(claster="МКН19"))
    paginate_by = 20


class FttxClasterAerodromView(ListView):
    model = Fttx
    queryset = (Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")
                .filter(claster="Аэродром"))
    paginate_by = 20
