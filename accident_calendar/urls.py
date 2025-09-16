from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('calendar/<int:slot_id>/', views.book_slot, name='book_slot'),
]