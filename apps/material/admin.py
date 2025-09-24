from .models import Material, ExpansionFttx, ExpansionWTTX, ChangeEquipment
from django.contrib import admin
from apps.accident.models import Area
from django import forms
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

class ExpansionFttxAdminForm(forms.ModelForm):
    """Custom form for Key model in admin interface."""
    city = forms.ModelChoiceField(
        queryset=Area.objects.all(),
        empty_label="Выберите город",
        required=True,
        to_field_name="city",
    )

    class Meta:
        model = ExpansionFttx
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.city:
            try:
                self.fields['city'].initial = Area.objects.get(city=self.instance.city)
            except Area.DoesNotExist:
                pass

    def clean_city(self):
        area = self.cleaned_data['city']
        return area.city if area else ""

@admin.register(ExpansionFttx)
class ExpansionFttxAdmin(admin.ModelAdmin):
    """Admin configuration for ExpansionFttx model."""
    form = ExpansionFttxAdminForm
    list_filter = ['city', 'street']
    search_fields = ['street']
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


class ExpansionWttxAdminForm(forms.ModelForm):
    """Custom form for Key model in admin interface."""
    city = forms.ModelChoiceField(
        queryset=Area.objects.all(),
        empty_label="Выберите город",
        required=True,
    )

    class Meta:
        model = ExpansionWTTX
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'city' in self.fields:
            if self.instance and self.instance.city:
                try:
                    area_instance = Area.objects.get(city=self.instance.city)
                    self.fields['city'].initial = area_instance.pk
                except Area.DoesNotExist:
                    self.fields['city'].initial = None
        else:
            logger.error("[ERROR] Field 'city' not found in ExpansionWttxAdminForm self.fields during __init__")

    def clean_city(self):
        area = self.cleaned_data['city']
        return area.city if area else ""

@admin.register(ExpansionWTTX)
class ExpansionWttxAdmin(admin.ModelAdmin):
    """Admin configuration for ExpansionFttx model."""
    form = ExpansionWttxAdminForm
    list_filter = ['city', 'type_of_wifi', 'organization']
    search_fields = ['city', 'type_of_wifi', 'organization']
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


class ChangeEquipmentAdminForm(forms.ModelForm):
    """Custom form for Key model in admin interface."""
    city = forms.ModelChoiceField(
        queryset=Area.objects.all(),
        empty_label="Выберите город",
        required=True,
    )

    class Meta:
        model = ChangeEquipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'city' in self.fields:
            if self.instance and self.instance.city:
                try:
                    area_instance = Area.objects.get(city=self.instance.city)
                    self.fields['city'].initial = area_instance.pk
                except Area.DoesNotExist:
                    self.fields['city'].initial = None
        else:
            logger.error("[ERROR] Field 'city' not found in ChangeEquipmentAdminForm self.fields during __init__")

    def clean_city(self):
        area = self.cleaned_data['city']
        return area.city if area else ""

@admin.register(ChangeEquipment)
class ChangeEquipmentAdmin(admin.ModelAdmin):
    """Admin configuration for ChangeEquipment model."""
    form = ExpansionFttxAdminForm
    list_filter = ['city', 'street', 'type_of_equipment', 'organization']
    search_fields = ['city', 'street', 'type_of_equipment', 'organization']
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


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    """Admin configuration for Material model."""
    list_filter = ['city', 'organization_id']
    search_fields = ['city', 'organization_id']
    list_per_page = 20

    def get_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return [field.name for field in self.model._meta.fields if field.name != 'id']

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return []
