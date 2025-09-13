from django.urls import path
from rest_framework.routers import DefaultRouter

from api.incident.views import AccidentListByStatus, AccidentListByOrganization, AccidentCreateView, GetAccidentById, \
    AccidentListByNumber, AccidentPartialUpdateByNumber, AccidentDeleteByNumber

router = DefaultRouter()
router.register("status", AccidentListByStatus, basename="accidents-by-status")
router.register("organization", AccidentListByOrganization, basename="accidents-by-organization")
router.register("accident-create", AccidentCreateView, basename="accident-create")

urlpatterns = [
    path("<int:id>/", GetAccidentById.as_view(), name="incident-detail"),
    path("number/", AccidentListByNumber.as_view({"get": "retrieve"}), name="accident-by-number"),
    path(
        "partial_update/",
        AccidentPartialUpdateByNumber.as_view({"patch": "partial_update"}),
        name="accident-partial-update"
    ),
    path(
        "accidents-delete/",
        AccidentDeleteByNumber.as_view({"delete": "delete"}),
        name="accident-delete-by-number",
    )

]

urlpatterns += router.urls
