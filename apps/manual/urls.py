from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.ManualListView.as_view(),
        name="manual-list"
    ),
    path(
        "huawei/<int:pk>",
        views.ManualDetailView.as_view(),
        name="manual-detail-list"
    ),
]
