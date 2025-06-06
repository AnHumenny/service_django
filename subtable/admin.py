from django.contrib import admin

from subtable.models import SubOrganization

# Register your models here.

@admin.register(SubOrganization)
class SubOrg(admin.ModelAdmin):
    search_fields = ['name', 'type_of_work']