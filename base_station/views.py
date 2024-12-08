from .models import BaseStation

from django.views.generic import (
    ListView,
)


class BaseStationListView(ListView):
    model = BaseStation
    queryset = BaseStation.objects.all().order_by("id").values("id", "number", "city", "address")
    paginate_by = 25


class BaseStationLisGomelView(ListView):
    model = BaseStation
    queryset = BaseStation.objects.filter(city="Гомель").values("id", "number", "city", "address")
    paginate_by = 25


class BaseStationLisMinskView(ListView):
    model = BaseStation
    queryset = BaseStation.objects.filter(city="Минск").values("id", "number", "city", "address")
    paginate_by = 25

