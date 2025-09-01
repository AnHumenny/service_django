from django.urls import path

from api.user.views import UsersList

urlpatterns = [
    path("", UsersList.as_view(), name="users-list"),
]
