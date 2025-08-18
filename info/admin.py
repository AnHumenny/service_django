from django.contrib import admin
from accident.models import Area
from .models import Info
from django import forms
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

class InfoAdminForm(forms.ModelForm):
    """Custom form for Info model in admin interface."""
    city = forms.ModelChoiceField(
        queryset=Area.objects.all(),
        empty_label="Выберите город",
        required=True,
        to_field_name="city",
    )

    class Meta:
        model = Info
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


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    """Admin configuration for Info model."""
    form = InfoAdminForm
    list_filter = ['city', 'street']
    search_fields = ['street', 'claster']
    list_per_page = 30

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

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

    def has_delete_permission(self, request, obj=None):
        """Disable delete for non-superusers"""
        return request.user.is_superuser

    def has_add_permission(self, request):
        """Disable add for non-superusers"""
        return request.user.is_superuser
