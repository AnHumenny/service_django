from django.urls import path
from filewiever import views


urlpatterns = [
    path('', views.start_filebrowser, name='index_list'),
    path('gomel/', views.file_gomel, name='gomel'),
    path('download/<str:file>/', views.file_download_dlink, name='file_download_dlink'),
    path('ubiquity/download/<str:file>/', views.file_download_ubiquity, name='file_download_ubiquity'),
    path('client/download/<str:file>/', views.file_download_client, name='file_download_client'),
    path('railway/download/<str:file>/', views.file_download_railway, name='file_download_railway'),
    path('instruction/download/<str:file>/', views.file_download_instruction, name='file_download_instruction'),
]
