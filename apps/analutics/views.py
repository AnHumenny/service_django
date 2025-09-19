from django.shortcuts import render
from apps.analutics.logic import actual, vertical, all_year, line
from datetime import date


def actual_time():
    now = date.today()
    return now


def actual_year(request):
    """набор js-chart"""
    now = actual_time()
    dat_year = actual(now)
    answer = vertical(now)
    answer_year = all_year()
    answer_data = line(now.year)
    return render(request, "analutic/all_analutic.html",
                  { "date_year": dat_year, "month": answer[0], "dat_count": answer[1],
                    "year": answer_year[0], "count": answer_year[1], "data": answer_data["data"],"now_year": now.year,
                    "old_1": now.year - 1, "data_1": answer_data["data_1"], "old_2": now.year - 2,
                    "data_2": answer_data["data_2"], "old_3": now.year - 3, "data_3": answer_data["data_3"],
                    "old_4": now.year - 4, "data_4": answer_data["data_4"],})
