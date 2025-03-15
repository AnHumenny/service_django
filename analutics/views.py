from django.shortcuts import render
from analutics.logic import actual, vertical, all_year, line
from datetime import date


def actual_time():
    now = date.today()
    return now


def actual_year(request):
    """js-chart графика fttx на текущий год, круговой график с разбивкой по месяцам"""
    now = actual_time()
    dat_year = actual(now)
    return render(request, "analutic/analutic_list.html",
                  {"now_year": now.year, "date_year": dat_year})


def vertical_bar(request):
    """js-chart графика fttx на текущий год, столбчатый график по адресам"""
    now = actual_time()
    answer = vertical(now)
    return render(request, "analutic/vertical.html", {"month": answer[0], "dat_count": answer[1]})


def year(request):
    """js-chart графика fttx, круговой график с разбивкой по годам, выборка за последние 5 лет"""
    answer = all_year()
    return render(request, "analutic/all_year.html", {"year": answer[0], "count": answer[1]})


def line_year(request):
    """js-chart графика fttx, линейный график с разбивкой по годам и месяцам, выборка за последние 5 лет"""
    now = actual_time()
    answer = line(now.year)
    return render(request, "analutic/line.html", {
        "now_year": now.year,
        "data": answer["data"],
        "old_1": now.year - 1,
        "data_1": answer["data_1"],
        "old_2": now.year - 2,
        "data_2": answer["data_2"],
        "old_3": now.year - 3,
        "data_3": answer["data_3"],
        "old_4": now.year - 4,
        "data_4": answer["data_4"],
    })
