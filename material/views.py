from django.core.paginator import Paginator
from django.shortcuts import render
from .logic import all_material, exp_fttx, exp_wttx


def material_page(request):
    material = all_material()
    paginator = Paginator(material, per_page=10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    expansion_fttx = exp_fttx()
    expansion_wttx = exp_wttx()

    return render(request, "material/material_list.html", {
        "page_obj": page_obj,
        "material": material,
        "expansionfttx": expansion_fttx,
        "expansionwttx": expansion_wttx,
    })
