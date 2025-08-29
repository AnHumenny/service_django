from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    """Inline user profile in the admin panel"""
    model = Profile
    can_delete = False
    verbose_name_plural = "Профиль"
    fk_name = "user"


class UserAdmin(BaseUserAdmin):
    """Custom user admin panel with organization display"""
    inlines = (ProfileInline,)
    list_display = ("username", "email", "first_name", "last_name", "get_organization", "is_staff")

    def get_organization(self, obj):
        return obj.profile.organization if hasattr(obj, "profile") and obj.profile.organization else "-"
    get_organization.short_description = "Организация"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
