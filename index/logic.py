from datetime import datetime
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.utils import timezone
from info.models import Info
from accident.models import Accident
from .models import Index, Material, ExpansionFttx, ExpansionWTTX
from datetime import date

now = date.today()
start_date = timezone.datetime(now.year, 1, 1)
end_date = timezone.datetime(now.year, 12, 31)
current_year = datetime.now().year
current_date = datetime.now().strftime("%Y-%m-%d")


def ind():
    """сплетни главной страницы"""
    query = Index.objects.order_by("-id")[:30]
    return query


def all_cable():
    """сборка utp по месяцам текущего года"""
    res_cable = (Info.objects.values("street").filter(date_created__range=(start_date, end_date)).annotate(
        month=TruncMonth('date_created')).values('city', 'month')
                    .annotate(total_amount=Sum('cable_1') + Sum('cable_2') + Sum("cable_3")).order_by('month'))
    return res_cable


def total_cable():
    """Общая сумма utp за год"""
    total_cable_sum = (
                          Info.objects
                          .filter(date_created__range=(start_date, end_date))
                          .aggregate(
                              total=Sum('cable_1') + Sum('cable_2') + Sum('cable_3')
                          )
                      )['total'] or 0
    return total_cable_sum


def total_utp():
    """суммарный метраж utp по году"""
    total_sum = (
                      Material.objects
                      .filter(date__year=current_year)
                      .aggregate(total_cable=Sum('cable'))
                  )['total_cable'] or 0
    return total_sum


def data_obj():
    data_object = (Info.objects.filter(date_created__range=(start_date, end_date)).order_by("-id").
                values("id", "reestr", "date_created", "city", "street", "home", "apartment", "name", ))
    return data_object


def result_exp():
    """расширение fttx"""
    res_exp = (
        ExpansionFttx.objects
        .filter(date__year=current_year)
        .aggregate(total_cable=Sum('cable'))
    )
    res_expansion = res_exp['total_cable']
    return res_expansion


def res_expansion_wttx():
    """'Cборка wttx"""
    expansion_wttx = (
        ExpansionWTTX.objects
        .filter(date__year=current_year)
        .aggregate(total_cable=Sum('cable'))
    )
    res_wttx = expansion_wttx['total_cable']
    return res_wttx


def expire():
    """разбор по месяцам"""
    res = (Info.objects.filter(date_created__range=(start_date, end_date))
         .annotate(month=TruncMonth('date_created'))
         .values('month')
         .annotate(count=Count('id')).order_by('month')
         )
    dat = []
    for row in res:
        temp = row.get("count")
        dat.append(int(temp))
    return dat


def accident_query():
    """блок инцидентов в статусе `Open`"""
    accident = Accident.objects.order_by("-id").filter(status="open")[:30]
    return accident


def check_query():
    """блок инцидентов в статусе `Check`"""
    query = Accident.objects.order_by("-id").filter(status="check")[:30]
    return query


def close_query():
    """блок инцидентов в статусе `Close`"""
    query = Accident.objects.order_by("-id").filter(status="close")[:30]
    return query
