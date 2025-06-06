from django.contrib import admin
from .models import BaseStation


@admin.register(BaseStation)
class InfoKey(admin.ModelAdmin):
    search_fields = ['city']
    list_per_page = 30

    def get_fields(self, request, obj=None):
        return ['number', 'city', 'address', 'comment']

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['number', 'city', 'address', 'comment']
        return []
