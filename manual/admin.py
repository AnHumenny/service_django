from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Manual

@admin.register(Manual)
class InfoManual(admin.ModelAdmin):
    search_fields = ['model']
    list_per_page = 30

    def get_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return ['type', 'model', 'rendered_description']
        return ['type', 'model', 'description']

    def get_readonly_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return ['type', 'model', 'rendered_description']
        return []

    def rendered_description(self, obj):
        return mark_safe(obj.description)
    rendered_description.short_description = "Описание"
