from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView

from accident.models import Accident
from .logic import all_material, exp_fttx, exp_wttx, change_equip
from .models import ChangeEquipment


def material_page(request):
    material = all_material()
    paginator = Paginator(material, per_page=10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    expansion_fttx = exp_fttx()
    expansion_wttx = exp_wttx()
    change_equipment = change_equip()


    return render(request, "material/material_list.html", {
        "page_obj": page_obj,
        "material": material,
        "expansionfttx": expansion_fttx,
        "expansionwttx": expansion_wttx,
        "equipment": change_equipment
    })


class EquipmentDetailView(DetailView):
    """Детальная информация по замене оборудования (по id)"""
    model = ChangeEquipment
    template_name = "material/equipment_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return obj


class EquipmentAccidentDetailView(DetailView):
    model = ChangeEquipment
    template_name = "accident/accident_detail.html"

    def get_object(self, queryset=None):
        number = self.kwargs.get('number')
        try:
            obj = Accident.objects.get(number=number)
        except Accident.DoesNotExist:
            raise Http404(f"ChangeEquipment с number {number} не найден")
        return obj
