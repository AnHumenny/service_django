from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.actual_year,
        name="actual-stat"
    ),
]
