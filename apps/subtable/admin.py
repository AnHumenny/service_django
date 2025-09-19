from django.contrib import admin
from apps.subtable.models import SubOrganization, SubNameEquipment, SubTypeEquipment


@admin.register(SubOrganization)
class SubOrg(admin.ModelAdmin):
    search_fields = ['name', 'type_of_work']

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


@admin.register(SubNameEquipment)
class SubNameEquipment(admin.ModelAdmin):
    search_fields = ['name_of_equipment']

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


@admin.register(SubTypeEquipment)
class SubTypeEquipment(admin.ModelAdmin):
    search_fields = ['type_of_equipment']

    def get_fields(self, request, obj=None):
        """Return editable fields based on user permissions."""
        if request.user.is_superuser:
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return []

    def get_readonly_fields(self, request, obj=None):
        """Return fields that are read-only for non-superusers."""
        if not request.user.is_superuser:
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return []
