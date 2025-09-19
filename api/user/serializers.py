from rest_framework import serializers

from apps.user_setting.models import Profile


class UsersSerializer(serializers.ModelSerializer):
    """Serializer for the Profile model.
    Includes all user profile fields."""

    class Meta:
        model = Profile
        fields = "__all__"
