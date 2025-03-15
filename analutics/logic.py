from django.db.models import Count
from django.db.models.functions import TruncMonth, ExtractYear
from django.utils import timezone
from info.models import Info
from datetime import date, datetime

def actual(now):
    """js-chart графика fttx  на текущий год, круговой график с разбивкой по месяцам"""
    start_date = timezone.datetime(now.year, 1, 1)
    end_date = timezone.datetime(now.year, 12, 31)
    l = (Info.objects
         .filter(date_created__range=(start_date, end_date))
         .annotate(month=TruncMonth('date_created'))
         .values('month')
         .annotate(count=Count('id')).order_by('month'))
    dat_year = []
    for row in l:
        temp = row.get("count")
        dat_year.append(int(temp))
    return dat_year


def vertical(now):
    """js-chart графика fttx на текущий год, столбчатый график по адресам"""
    start_date = timezone.datetime(now.year, 1, 1)
    end_date = timezone.datetime(now.year, 12, 31)
    s = (Info.objects
         .filter(date_created__range=(start_date, end_date))
         .annotate(month=TruncMonth('date_created'))
         .values('street')
         .annotate(count=Count('id'))
         .order_by('street'))
    month = []
    dat_count = []
    for row in s:
        temp = row.get("count")
        street = row.get("street")
        month.append(street.strip())
        dat_count.append(int(temp))
    return month, dat_count


def all_year():
    """js-chart графика fttx, круговой график с разбивкой по годам, выборка за последние 5 лет"""
    year = (
        Info.objects
        .annotate(year=ExtractYear('date_created'))
        .values('year')
        .annotate(count=Count('id'))
        .order_by('year')
    )
    years = []
    count = []
    for row in year:
        y = row.get("year")
        years.append(y)
        c = row.get("count")
        count.append(c)
    return years, count


def line(now):
    """js-chart графика fttx, линейный график с разбивкой по годам и месяцам, выборка за последние 5 лет"""
    dat_year_now = (
        Info.objects.filter(date_created__year=now)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    data_now = [int(row.get("count")) for row in dat_year_now]

    dat_year_1 = (
        Info.objects.filter(date_created__year=now - 1)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    data_1 = [int(row.get("count")) for row in dat_year_1]

    dat_year_2 = (
        Info.objects.filter(date_created__year=now - 2)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    data_2 = [int(row.get("count")) for row in dat_year_2]

    dat_year_3 = (
        Info.objects.filter(date_created__year=now - 3)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    data_3 = [int(row.get("count")) for row in dat_year_3]

    dat_year_4 = (
        Info.objects.filter(date_created__year=now - 4)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    data_4 = [int(row.get("count")) for row in dat_year_4]

    return {
        "data": data_now,
        "data_1": data_1,
        "data_2": data_2,
        "data_3": data_3,
        "data_4": data_4,
    }
