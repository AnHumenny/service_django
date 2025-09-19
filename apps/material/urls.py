from django.urls import path

from . import views
from .views import material_page

urlpatterns = [
    path('', material_page, name='material_page'),
    path(
        "change/<int:pk>",
        views.EquipmentDetailView.as_view(),
        name="change-detail"
    ),
    path("<str:number>/", views.EquipmentAccidentDetailView.as_view(), name="ass-detail")
]
