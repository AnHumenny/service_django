from django.contrib import admin

from .models import Material, ExpansionFttx, ExpansionWTTX, ChangeEquipment

admin.site.register(Material)
admin.site.register(ExpansionFttx)
admin.site.register(ExpansionWTTX)
admin.site.register(ChangeEquipment)
