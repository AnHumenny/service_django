from .models import Key

from django.views.generic import (
    ListView,
)


class KeyListView(ListView):
    model = Key
    key = Key.objects.order_by("id").values("city")
    paginate_by = 40
