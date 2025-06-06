from django.contrib import admin
from .models import Fttx

@admin.register(Fttx)
class InfoFttx(admin.ModelAdmin):
    list_filter = ['city', 'street']
    search_fields = ['street', 'claster']
    list_per_page = 20

    def get_fields(self, request, obj=None):
        return ['city', 'claster', 'street', 'number', 'description', 'askue']

    def get_readonly_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return ['city', 'claster', 'street', 'number', 'description', 'askue']
        return []