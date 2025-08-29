from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    GetAccidentById, AccidentListByStatus, AccidentListByOrganization,
    AccidentDeleteByNumber, AccidentListByNumber, AccidentPartialUpdateByNumber
)

router = DefaultRouter()
router.register("status", AccidentListByStatus, basename="accidents-by-status")
router.register("organization", AccidentListByOrganization, basename="accidents-by-organization")
router.register("delete", AccidentDeleteByNumber, basename="accidents-delete")

urlpatterns = [
    path("<int:id>/", GetAccidentById.as_view(), name="incident-detail"),
    path("number/", AccidentListByNumber.as_view({"get": "retrieve"}), name="accident-by-number"),
    path(
        "partial_update/",
        AccidentPartialUpdateByNumber.as_view({"patch": "partial_update"}),
        name="accident-partial-update"
    ),

]

urlpatterns += router.urls
