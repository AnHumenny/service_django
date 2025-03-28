"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #Импортируем функцию include.

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("index.urls")),  
    path('accident/', include('accident.urls')),
    path('info/', include('info.urls')),
    path('key/', include('key.urls')),
    path('base_station/', include('base_station.urls')),
    path('gazprom/', include('gazprom.urls')),
    path('manual/', include('manual.urls')),
    path('fttx/', include('fttx.urls')),
    path('api/', include('api.urls')),
    path('analutics/', include('analutics.urls')),
    path('filewiever/', include('filewiever.urls')),
    path('material/', include('material.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
]
