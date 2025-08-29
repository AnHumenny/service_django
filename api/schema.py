from drf_spectacular.utils import extend_schema, OpenApiParameter
from api.incident.serializers import AccidentGetSerializer, AccidentUpdateSerializer
from api.user.serializers import UsersSerializer


def extend_schema_accident_by_id():
    """Returns data for a single incident by its ID."""
    return extend_schema(
        summary="Получить инцидент по ID",
        description="Возвращает данные одного инцидента по его ID",
        responses=AccidentGetSerializer(many=True),
        tags=["Accident"]
    )


def extend_schema_accident_by_number():
    """Returns data of one incident by its number."""
    return extend_schema(
        summary="Получить инцидент по номеру",
        description="Возвращает данные одного инцидента по его number",
        parameters=[
            OpenApiParameter(
                name="number",
                type=str,
                required=True,
                description="Номер инцидента",
            )
        ],
        responses=AccidentGetSerializer(many=True),
        tags=["Accident"]
    )


def extend_schema_accident_by_status():
    """Returns a list of incidents with the specified status: 'open' or 'check'."""
    return extend_schema(
        summary="Список инцидентов по статусу",
        description="Возвращает список инцидентов с указанным статусом: 'open' или 'check'.",
        parameters=[
            OpenApiParameter(
                name="status",
                type=str,
                required=True,
                description="Статус инцидента: 'open' или 'check'",
            )
        ],
        responses=AccidentGetSerializer(many=True),
        tags=["Accident"]
    )


def extend_schema_accident_by_organization():
    """Returns a list of incidents filtered by organization and status ('open' or 'check')."""
    return extend_schema(
        summary="Список инцидентов по организации и статусу",
        description="Возвращает список инцидентов с фильтром по организации и статусу ('open' или 'check').",
        parameters=[
            OpenApiParameter(
                name="organization",
                type=str,
                required=True,
                description="Название организации для фильтрации инцидентов",
            ),
            OpenApiParameter(
                name="status",
                type=str,
                required=True,
                description="Статус инцидента: 'open' или 'check'",
            ),
        ],
        responses=AccidentGetSerializer(many=True),
        tags=["Accident"],
    )


def extend_schema_update_accident_by_number():
    return extend_schema(
        summary="Частичное обновление инцидента по number",
        description="Updates the datetime_close, decide, and status fields of the incident with the specified number",
        parameters=[
            OpenApiParameter(
                name="number",
                type=str,
                required=True,
                description="Номер инцидента для обновления",
            )
        ],
        request=AccidentUpdateSerializer,
        responses=AccidentUpdateSerializer,
        tags=["Accident"]
    )


def extend_schema_list_of_users():
    """Returns a list of registered users"."""
    return extend_schema(
        summary="Список пользователей",
        description="Возвращает список зарегистрированных пользователей",
        responses=UsersSerializer,
        tags=["Users"],
    )

def extend_schema_delete_accident_by_number():
    """Deleted accident by number."""
    return extend_schema(
        summary="Удаление инцидента по number",
        description="Удаление инцидента по номеру",
        responses=AccidentGetSerializer(many=True),
        parameters=[
            OpenApiParameter(
                name="number",
                type=str,
                required=True,
                description="Номер инцидента для удаления",
            )
        ],
        tags=["Accident"]
    )
