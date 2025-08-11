from django.contrib import admin
from google_calendar.google_calendar import create_google_calendar_event
from .models import Accident, AccidentStatus, Area
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class AccidentAdminForm(forms.ModelForm):
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
    form = AccidentAdminForm
    list_filter = ['status']
    search_fields = ['number', 'city__city', 'name', 'subscriber', 'comment']
    list_per_page = 20

    def get_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return [
                'number', 'category', 'sla', 'datetime_open', 'datetime_close', 'problem', 'address',
                'city', 'phone', 'subscriber', 'name', 'comment', 'decide', 'organization', 'status'
            ]
        return [
            'number', 'category', 'sla', 'datetime_open', 'datetime_close', 'problem', 'address',
            'city', 'phone', 'subscriber', 'name', 'comment', 'decide', 'organization', 'status'
        ]

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.status == AccidentStatus.CLOSE and not request.user.is_superuser:
            return [
                'number', 'category', 'sla', 'datetime_open', 'datetime_close', 'problem', 'address',
                'city', 'phone', 'subscriber', 'name', 'comment', 'decide', 'organization', 'status'
            ]
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
    list_display = ['city']
    search_fields = ['city']
