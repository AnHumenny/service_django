from material.models import Material, ExpansionFttx, ExpansionWTTX


def all_material():
    """запрашиваем остатки(приход)" по всем материалам"""
    mat = Material.objects.all().order_by("-id")
    return mat

def exp_fttx():
    """расширение fttx"""
    fttx = ExpansionFttx.objects.all().order_by("-id")
    return fttx

def exp_wttx():
    """монтаж оборудования wttx"""
    wttx = ExpansionWTTX.objects.all().order_by("-id")
    return wttx
