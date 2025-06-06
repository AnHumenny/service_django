from django.contrib import admin
from .models import Gazprom

@admin.register(Gazprom)
class InfoGazprom(admin.ModelAdmin):
    search_fields = ['city']
    list_per_page = 30

    def get_fields(self, request, obj=None):
        return ['ip', 'number', 'type', 'region', 'address', 'comment', 'geo']

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['ip', 'number', 'type', 'region', 'address', 'comment', 'geo']
        return []
