from rest_framework import serializers
from accident.models import Accident


class AccidentGetSerializer(serializers.ModelSerializer):
    """Serializer for retrieving all fields of an accident."""
    class Meta:
        model = Accident
        fields = "__all__"


class AccidentPostSerializer(serializers.ModelSerializer):
    """Serializer for creating a new accident with selected fields."""
    class Meta:
        model = Accident
        fields = (
            "id", "category", "sla", "datetime_open", "datetime_close",
            "problem", "city", "address", "name", "phone",
            "subscriber", "comment", "status", "organization"
        )


class AccidentUpdateSerializer(serializers.ModelSerializer):
    """Serializer for partially updating an accident (close time, decision, status)."""
    class Meta:
        model = Accident
        fields = ("datetime_close", "decide", "status")
