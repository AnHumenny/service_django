from django.contrib import admin
from google_calendar.google_calendar import create_google_calendar_event
from .models import Accident, AccidentStatus, Area
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class AccidentAdminForm(forms.ModelForm):
    """Custom form for Accident model in admin interface."""

    city = forms.ModelChoiceField(
        queryset=Area.objects.all(),
        empty_label="Выберите город",
        required=True,
    )

    class Meta:
        model = Accident
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.city:
            try:
                area_instance = Area.objects.get(city=self.instance.city)
                self.fields['city'].initial = area_instance.pk
            except Area.DoesNotExist:
                pass

    def clean_city(self):
        area = self.cleaned_data['city']
        return area.city


@admin.register(Accident)
class AccidentAdmin(admin.ModelAdmin):
    """Admin configuration for Accident model."""
    form = AccidentAdminForm
    list_filter = ['city']
    search_fields = ['number', 'city__city', 'name', 'subscriber', 'comment']
    list_per_page = 20
    change_list_template = "admin/accident/change_list.html"

    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['show_google_link'] = request.user.is_superuser
        return super().changelist_view(request, extra_context=extra_context)

    def get_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return [field.name for field in self.model._meta.fields if field.name != 'id']

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.status == AccidentStatus.CLOSE and not request.user.is_superuser:
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return []

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            create_google_calendar_event(
                user=request.user,
                number=obj.number,
                category=obj.category,
                sla=obj.sla,
                problem=obj.problem,
                city=obj.city,
                address=obj.address,
                datetime_open=obj.datetime_open,
                datetime_close=obj.datetime_close,
                name=obj.name,
                phone=obj.phone,
                description=obj.comment or ""
            )


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    """Admin configuration for Area model with city display and search."""
    list_display = ['city']
    search_fields = ['city']


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

    def has_delete_permission(self, request, obj=None):
        """Disable delete for non-superusers"""
        return request.user.is_superuser

    def has_add_permission(self, request):
        """Disable add for non-superusers"""
        return request.user.is_superuser
