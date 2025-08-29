from django.urls import path
from . import views


urlpatterns = [
    path('', views.AccidentListView.as_view(), name='accident-list'),
    path('<int:pk>/', views.AccidentDetailView.as_view(), name='accident-detail'),
    path('open/', views.AccidentOpenView.as_view(), name='accident-open-list'),
    path('close/', views.AccidentCloseView.as_view(), name='accident-close-list'),
    path('check/', views.AccidentCheckView.as_view(), name='accident-check-list'),
    path('csv/actual/', views.download_actual_accident, name='download_actual_accident'),
    path('csv/previos/', views.download_previos_accident, name='download_previos_accident'),
]
