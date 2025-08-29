from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from api.user.serializers import UsersSerializer
from user_setting.models import Profile


class UsersList(ListAPIView):
    """API endpoint for getting a list of users with profiles."""
    queryset = Profile.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
