from rest_framework.permissions import BasePermission

class IsContractor(BasePermission):
    """Access only for users from the Contractor group."""

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Contractor").exists()
        )
