from django.contrib import admin
from .models import Gazprom

@admin.register(Gazprom)
class InfoGazprom(admin.ModelAdmin):
    search_fields = ['city']
    list_per_page = 30

    def get_fields(self, request, obj=None):
        """Return editable fields based on user permissions."""
        return [field.name for field in self.model._meta.fields if field.name != 'id']

    def get_readonly_fields(self, request, obj=None):
        """Return fields that are read-only for non-superusers."""
        if obj is not None:
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return []

    def has_delete_permission(self, request, obj=None):
        """Disable delete for non-superusers"""
        return request.user.is_superuser

    def has_add_permission(self, request):
        """Disable add for non-superusers"""
        return request.user.is_superuser
