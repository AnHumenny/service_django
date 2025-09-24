from django.urls import path
# from . import views
from .google_calendar import fetch_google_events
from .oauth import start_google_auth, google_calendar_callback

urlpatterns = [
        # path('posts/', views.calendar_list, name='calendar_list'),
        # path('posts/<int:post_id>/', views.calendar_detail, name='calendar_detail'),
        path('start/', start_google_auth, name='start_google_auth'),
        path('callback/', google_calendar_callback, name='google_calendar_callback'),
        path('fetch_events/', fetch_google_events, name='fetch_google_events'),
    ]
