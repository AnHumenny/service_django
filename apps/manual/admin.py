from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Manual

@admin.register(Manual)
class InfoManual(admin.ModelAdmin):
    search_fields = ['model']
    list_per_page = 30

    def get_fields(self, request, obj=None):
        """Return editable fields based on user permissions.
        Shows all fields for superusers during add or edit; none for others."""
        if request.user.is_superuser:
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return []

    def get_readonly_fields(self, request, obj=None):
        """Return fields that are read-only for non-superusers."""
        if not request.user.is_superuser:
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return []

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

    def has_delete_permission(self, request, obj=None):
        """Disable delete for non-superusers"""
        return request.user.is_superuser

    def has_add_permission(self, request):
        """Disable add for non-superusers"""
        return request.user.is_superuser

    def rendered_description(self, obj):
        return mark_safe(obj.description)
    rendered_description.short_description = "Описание"
