from datetime import datetime
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.utils import timezone
from fttx.models import Fttx
from info.models import Info
from accident.models import Accident
from key.models import Key
from manual.models import Manual
from .models import Index
from material.models import Material, ExpansionFttx, ExpansionWTTX
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
    """Краткая сводка по последним абонам FTTx"""
    data_object = (Info.objects.filter(date_created__range=(start_date, end_date))
                   .order_by("-id")
                   .values(
                       "id",
                       "reestr",
                       "date_created",
                       "city",
                       "street",
                       "home",
                       "apartment",
                       "name",
                       "organization__name"
                   ))[:10]
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


def info_search(result):
    """поиск в БД info_info (абоненты (ФИО))"""
    answer = Info.objects.filter(name__icontains=result).filter(name__icontains=result)
    return answer


def incident_number(result):
    """Поиск в инцидентах по номеру заявки"""
    answer = Accident.objects.filter(number=result).order_by("id")
    if answer is None:
        return None
    return answer


def incident_name(result):
    """Поиск в инцидентах по ФИО"""
    res = result.split(" ")
    if len(res) == 3:
        answer = Accident.objects.filter(name=result).order_by("id")
    else:
        return None
    return answer


def incident_addr(result):
    """Поиск в инцидентах по адресу"""
    address = result.split(", ", 1)
    first_addr = address[0].strip()
    second_addr = address[1].strip()
    if len (address) != 2:
        return None
    answer = Accident.objects.filter(city=first_addr, address=second_addr)
    if not answer.exists():
        return None
    else:
        return answer


def man(result):
    """поиск в мануалах"""
    answer = Manual.objects.filter(type__icontains=result)
    if not answer.exists():
        return None
    else:
        return answer


def search_in_fttx(result):
    """поиск в fttx_fttx (подробная информация fttx по адресам)"""
    result = result.split(", ")
    answer = Fttx.objects.filter(city=result[0], street=result[1], number=result[2]).first()
    if answer is None:
        return None
    else:
        return answer

def search_in_key(result):
    """целевой поиск в ключах по адресу"""
    res_key = result.split(", ")
    answer = Key.objects.filter(city=res_key[0], street=res_key[1], home=res_key[2]).first()
    if answer is None:
        return None
    else:
        return answer
