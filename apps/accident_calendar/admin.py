from django.contrib import admin
from .models import TimeSlot


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    """Timeslot for events."""

    list_display = ('date', 'start_time', 'end_time', 'is_booked', 'booked_by', 'created_at')
    list_filter = ('date', 'is_booked')
    search_fields = ('date', 'booked_by__username')
    date_hierarchy = 'date'
    ordering = ('date', 'start_time')
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('date', 'start_time', 'end_time', 'is_booked', 'booked_by')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
