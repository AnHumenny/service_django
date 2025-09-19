from django.db import models
from django.contrib.auth import get_user_model
from apps.subtable.models import SubOrganization

User = get_user_model()

class Profile(models.Model):
    """Users profiles"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_setting_profile')
    organization = models.ForeignKey(
        SubOrganization,
        on_delete=models.CASCADE,
        related_name="profiles",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Profile of {self.user.username}"
