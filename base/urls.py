from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import urls as auth_urls

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.index.urls")),
    path('accident/', include('apps.accident.urls')),
    path('info/', include('apps.info.urls')),
    path('key/', include('apps.key.urls')),
    path('base_station/', include('apps.base_station.urls')),
    path('gazprom/', include('apps.gazprom.urls')),
    path('manual/', include('apps.manual.urls')),
    path('fttx/', include('apps.fttx.urls')),
    path('analutics/', include('apps.analutics.urls')),
    path('filewiever/', include('apps.filewiever.urls')),
    path('material/', include('apps.material.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('grappelli/', include('grappelli.urls')),
    path("google_calendar/", include("apps.google_calendar.urls")),
    path('accident_calendar/', include('apps.accident_calendar.urls')),


    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/user/", include("api.user.urls")),
    path("api/incident/", include("api.incident.urls")),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]