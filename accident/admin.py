from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Accident, AccidentStatus


@admin.register(Accident)
class AccidentAdmin(admin.ModelAdmin):
    list_filter = ['status']
    search_fields = ['number', 'city', 'name', 'subscriber', 'comment']
    list_per_page = 20

    def get_fields(self, request, obj=None):
        """Return the list of fields to display in the admin form."""
        if obj and not request.user.is_superuser:
            return ['number', 'category', 'sla', 'datetime_open', 'datetime_close', 'problem', 'address', 'city',
                    'phone', 'subscriber',  'name', 'comment', 'decide', 'organization', 'status']
        return ['number', 'category', 'sla', 'datetime_open', 'datetime_close', 'problem', 'address', 'city',
                    'phone', 'subscriber',  'name', 'comment', 'decide', 'organization', 'status']


    def get_readonly_fields(self, request, obj=None):
        """Make all fields read-only if status is close."""

        if (obj is not None and obj.status == AccidentStatus.CLOSE and not request.user.is_superuser
                and not request.user.is_superuser):
            return ['number', 'category', 'sla', 'datetime_open', 'datetime_close', 'problem', 'address', 'city',
                    'phone', 'subscriber',  'name', 'comment', 'decide', 'organization', 'status']
        return []
