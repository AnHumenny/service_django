from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    """Users profiles"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_setting_profile')

    def __str__(self):
        return f"Profile of {self.user.username}"
