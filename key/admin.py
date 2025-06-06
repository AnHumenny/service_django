from django.contrib import admin
from .models import Key

@admin.register(Key)
class InfoKey(admin.ModelAdmin):
    list_filter = ['city', 'street']
    search_fields = ['street']
    list_per_page = 20

    def get_fields(self, request, obj=None):
        return ['city', 'street', 'home', 'entrance', 'ind', 'stand']

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['city', 'street', 'home', 'entrance', 'ind', 'stand']
        return []
