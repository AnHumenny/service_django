from django.contrib import admin
from .models import Info


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_filter = ['city', 'street']
    search_fields = ['city', 'street', 'name']
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        """Make all fields read-only if status is close."""

        if obj is not None:
            return ['reestr', 'date_created', 'city', 'street', 'home', 'apartment', 'name', 'cable_1',
                    'cable_2', 'cable_3', 'connector' ]
        return []
