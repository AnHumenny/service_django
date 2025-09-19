from rest_framework import viewsets, status, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.accident.models import Accident, AccidentStatus
from api.incident.serializers import AccidentGetSerializer, AccidentUpdateSerializer
from api.schema import extend_schema_accident_by_status, extend_schema_accident_by_id, \
    extend_schema_accident_by_organization, extend_schema_accident_by_number, extend_schema_update_accident_by_number, \
    extend_schema_delete_accident_by_number, extend_schema_create_accident


@extend_schema_accident_by_id()
class GetAccidentById(generics.RetrieveAPIView):
    """Get accident by id as superadmin or affiliation with an organization"""
    serializer_class = AccidentGetSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Accident.objects.all()
        if hasattr(user, "user_setting_profile") and user.user_setting_profile.organization:
            return Accident.objects.filter(
                organization=user.user_setting_profile.organization
            )
        return Accident.objects.none()


@extend_schema_accident_by_number()
class AccidentListByNumber(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Get accident by number as superadmin or affiliation with an organization"""
    serializer_class = AccidentGetSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "number"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Accident.objects.all()
        if hasattr(user, "user_setting_profile") and user.user_setting_profile.organization:
            return Accident.objects.filter(
                organization=user.user_setting_profile.organization
            )
        return Accident.objects.none()

    def retrieve(self, request, *args, **kwargs):
        number_param = request.query_params.get("number")
        if not number_param:
            return Response(
                {"error": "Query parameter 'number' not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            accident = self.get_queryset().get(number=number_param)
        except Accident.DoesNotExist:
            return Response(
                {"error": f"Accident with number {number_param} not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(accident)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema_accident_by_status()
class AccidentListByStatus(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Get accident by status (open, check) as superadmin or by organization"""
    serializer_class = AccidentGetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        status_param = self.request.query_params.get("status")

        allowed_statuses = [AccidentStatus.OPEN, AccidentStatus.CHECK]

        if status_param not in allowed_statuses:
            return Accident.objects.none()

        if user.is_superuser:
            return Accident.objects.filter(status=status_param)

        if (
            hasattr(user, "user_setting_profile")
            and user.user_setting_profile.organization
        ):
            return Accident.objects.filter(
                organization=user.user_setting_profile.organization,
                status=status_param
            )
        return Accident.objects.none()

    def list(self, request, *args, **kwargs):
        status_param = request.query_params.get("status")
        if status_param not in [AccidentStatus.OPEN, AccidentStatus.CHECK]:
            return Response(
                {"error": "Query parameter 'status' must be 'open' or 'check'"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().list(request, *args, **kwargs)


@extend_schema_accident_by_organization()
class AccidentListByOrganization(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    View a list of accidents for a specific organization.
    Only superusers can retrieve the data. Other users have no access.
    Supports filtering by organization name and status (open, check).
    """

    serializer_class = AccidentGetSerializer
    permission_classes = [IsAuthenticated]

    VALID_STATUSES = [choice.value for choice in AccidentStatus if choice != AccidentStatus.CLOSE]

    def get_queryset(self):
        user = self.request.user

        if not user.is_superuser:
            return Accident.objects.none()

        queryset = Accident.objects.all()
        org_param = self.request.query_params.get("organization")
        status_param = self.request.query_params.get("status")

        if org_param:
            queryset = queryset.filter(organization__name=org_param)

        if status_param in self.VALID_STATUSES:
            queryset = queryset.filter(status=status_param)

        return queryset.order_by("-id")

    def list(self, request, *args, **kwargs):
        org_param = request.query_params.get("organization")
        if not org_param:
            return Response(
                {"error": "Query parameter 'organization' is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        status_param = request.query_params.get("status")
        if status_param and status_param not in self.VALID_STATUSES:
            return Response(
                {"error": f"Query parameter 'status' must be one of {self.VALID_STATUSES}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().list(request, *args, **kwargs)


@extend_schema_update_accident_by_number()
class AccidentPartialUpdateByNumber(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """Partial update of the incident by number."""
    serializer_class = AccidentUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "number"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Accident.objects.all()
        if hasattr(user, "user_setting_profile") and user.user_setting_profile.organization:
            return Accident.objects.filter(
                organization=user.user_setting_profile.organization
            )
        return Accident.objects.none()



@extend_schema_delete_accident_by_number()
class AccidentDeleteByNumber(viewsets.ViewSet):
    """Delete accident by number as superadmin"""
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        if not request.user.is_superuser:
            return Response(
                {"error": "Only superusers can delete accidents"},
                status=status.HTTP_403_FORBIDDEN
            )
        number_param = request.query_params.get("number")
        if not number_param:
            return Response(
                {"error": "Query parameter 'number' is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            accident = Accident.objects.get(number=number_param)
        except Accident.DoesNotExist:
            return Response(
                {"error": f"Accident with number {number_param} not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        accident.delete()
        return Response(
            {"message": f"Accident {number_param} deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )


@extend_schema_create_accident()
class AccidentCreateView(viewsets.ViewSet):
    """Create accident as superadmin"""
    permission_classes = [IsAuthenticated]

    def create(self, request):
        if not request.user.is_superuser:
            return Response(
                {"error": "Only superusers can create accidents"},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = AccidentGetSerializer(data=request.data)
        if serializer.is_valid():
            accident = serializer.save()
            return Response(
                AccidentGetSerializer(accident).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
