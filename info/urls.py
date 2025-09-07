from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.InfoListView.as_view(),
        name="info-list"
    ),
    path(
        "info/<int:pk>",
        views.InfoDetailView.as_view(),
        name="info-detail"
    ),
    path('csv/', views.date_range_view, name='date_range'),
]
