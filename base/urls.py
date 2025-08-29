from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.contrib import admin
from django.urls import path, include

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
    path('analutics/', include('analutics.urls')),
    path('filewiever/', include('filewiever.urls')),
    path('material/', include('material.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('grappelli/', include('grappelli.urls')),
    path("google_calendar/", include("google_calendar.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/user/", include("api.user.urls")),
    path("api/incident/", include("api.incident.urls")),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]