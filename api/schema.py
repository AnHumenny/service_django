from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from api.incident.serializers import AccidentGetSerializer, AccidentUpdateSerializer
from api.user.serializers import UsersSerializer


def extend_schema_accident_by_id():
    """Returns data for a single incident by its ID."""
    return extend_schema(
        summary="Получить инцидент по ID",
        description="Возвращает данные одного инцидента по его уникальному ID. "
                    "Поддерживает только активные инциденты. Если ID не найден, возвращает 404.",
        parameters=[
            OpenApiParameter(
                name="id",
                type=int,
                location='path',
                description="Уникальный ID инцидента",
                required=True,
            )
        ],
        responses={
            200: AccidentGetSerializer(many=False),
            404: OpenApiResponse(
                description="Инцидент не найден",
            )
        },
        tags=["Accident"],
        examples=[
            OpenApiExample(
                name="Success!",
                value={
                    "id": 12345,
                    "number": "IN00002014(str)",
                    "category": "ФИ-7(str)",
                    "sla": "срок ликвидации аварии(str)",
                    "datetime_open": "2025-05-12T14:36:57.530Z",
                    "datetime_close": "2025-16-08T06:36:57.530Z",
                    "problem": "Описание проблемы(str)",
                    "city": "Город(str)",
                    "address": "Адрес(str)",
                    "name": "контактные данные(str)",
                    "phone": "телефон(str)",
                    "subscriber": "абонентский номер(str)",
                    "comment": "комментарий техсаппорта(str)",
                    "decide": "решение(str)",
                    "status": "open(check, close(str))",
                    "organization": "int"
                },
                summary="Пример данных инцидента"
            )
        ]
    )


def extend_schema_accident_by_number():
    """Returns data of one incident by its number."""
    return extend_schema(
        summary="Получить инцидент по номеру",
        description="Возвращает данные одного инцидента по его number. Если ID не найден, возвращает 404.",
        parameters=[
            OpenApiParameter(
                name="number",
                type=str,
                location='query',
                description="Уникальный number инцидента",
                required=True,
            )
        ],
        responses={
            200: AccidentGetSerializer(many=False),
            404: OpenApiResponse(
                description="Инцидент не найден",
            )
        },
        tags=["Accident"],
        examples=[
            OpenApiExample(
                name="Success!",
                value={
                    "id": "IN00002014",
                    "number": "IN00002014(str)",
                    "category": "ФИ-7(str)",
                    "sla": "срок ликвидации аварии(str)",
                    "datetime_open": "2025-05-12T14:36:57.530Z",
                    "datetime_close": "2025-16-08T06:36:57.530Z",
                    "problem": "Описание проблемы(str)",
                    "city": "Город(str)",
                    "address": "Адрес(str)",
                    "name": "контактные данные(str)",
                    "phone": "телефон(str)",
                    "subscriber": "абонентский номер(str)",
                    "comment": "комментарий техсаппорта(str)",
                    "decide": "решение(str)",
                    "status": "open(check, close(str))",
                    "organization": "int"
                },
                summary="Пример данных инцидента"
            )
        ]
    )


def extend_schema_accident_by_status():
    """Returns a list of incidents with the specified status: 'open' or 'check'."""
    return extend_schema(
        summary="Список инцидентов по статусу",
        description="Возвращает список инцидентов с указанным статусом: 'open' или 'check'."
                    "Если инцидентов нет, возвращается пустой массив `[]`.",
        parameters=[
            OpenApiParameter(
                name="status",
                type=str,
                location='query',
                required=True,
                description="Статус инцидента: 'open' или 'check'",
            )
        ],
        responses={
            200: AccidentGetSerializer(many=True),
        },
        tags=["Accident"],
        examples=[

            OpenApiExample(
                name="Список инцидентов",
                value=[
                    {
                        "id": "IN00002014",
                        "number": "IN00002014",
                        "status": "open",
                        "datetime_open": "2025-05-12T14:36:57.530Z",
                        "problem": "Нет линка"
                    },
                    {
                        "id": "IN00002015",
                        "number": "IN00002015",
                        "status": "open",
                        "datetime_open": "2025-06-01T10:00:00.000Z",
                        "problem": "Отвал магистрали"
                    }
                ],
                summary="Сокращённый пример с двумя инцидентами "
                        "(остальные поля: category, city, sla и т.д. — см. схему)"
            ),

            OpenApiExample(
                name="Пустой список",
                value=[],
                summary="Нет инцидентов"
            )
        ]
    )


def extend_schema_accident_by_organization():
    """Returns a list of incidents filtered by organization and status ('open' or 'check')."""
    return extend_schema(
        summary="Список инцидентов по организации и статусу",
        description="Возвращает список инцидентов с фильтром по организации и статусу ('open' или 'check').",
        parameters=[
            OpenApiParameter(
                name="status",
                type=str,
                location='query',
                required=True,
                description="Статус инцидента: 'open' или 'check'",
            ),
        ],
        responses=AccidentGetSerializer(many=True),
        tags=["Accident"],
        examples=[

            OpenApiExample(
                name="Список инцидентов",
                value=[
                    {
                        "id": "IN00002014",
                        "number": "IN00002014",
                        "status": "open",
                        "datetime_open": "2025-05-12T14:36:57.530Z",
                        "problem": "Нет линка"
                    },
                    {
                        "id": "IN00002015",
                        "number": "IN00002015",
                        "status": "open",
                        "datetime_open": "2025-06-01T10:00:00.000Z",
                        "problem": "Отвал магистрали"
                    }
                ],
                summary="Сокращённый пример с двумя инцидентами "
                        "(остальные поля: category, city, sla и т.д. — см. схему)"
            ),

            OpenApiExample(
                name="Пустой список",
                value=[],
                summary="Нет инцидентов"
            )
        ]
    )


def extend_schema_update_accident_by_number():
    """Partial update accident by number."""
    return extend_schema(
        summary="Частичное обновление инцидента по number",
        description="Обновляет datetime_close, decide и status для инцидента с указанным номером",
        responses={
            200: AccidentUpdateSerializer(many=False),
            400: OpenApiResponse(
                description="Неверные данные в запросе (например, invalid status или дата)",
                examples=[
                    OpenApiExample(
                        name="Validation Error",
                        value={
                            "status": ["'open(check, close(str))' is not a valid choice."]
                        },
                        summary="Пример ошибки валидации поля status"
                    )
                ]
            ),
            404: OpenApiResponse(
                description="Инцидент не найден по указанному number"
            )
        },
        examples=[
            OpenApiExample(
                name="Request Body",
                value={
                    "datetime_close": "2025-06-08T06:36:57.530Z",
                    "decide": "Решение: полная замена оборудования",
                    "status": "check"
                },
                summary="Пример body для обновления"
            )
        ],
        request=AccidentUpdateSerializer,
        tags=["Accident"]
    )


def extend_schema_list_of_users():
    """Returns a list of registered users."""
    return extend_schema(
        summary="Список пользователей",
        description="Возвращает список зарегистрированных пользователей",
        responses=UsersSerializer,
        tags=["Users"],
    )


def extend_schema_delete_accident_by_number():
    """Delete accident by number."""
    return extend_schema(
        summary="Удаление инцидента по номеру",
        description="Удаляет инцидент по указанному номеру (query-параметр). "
                    "Требует аутентификации (admin права). "
                    "Успех: 204 (пустой ответ) или 200 с подтверждением. "
                    "Если инцидент не найден — 404. Удаление необратимо!",
        parameters=[
            OpenApiParameter(
                name="number",
                location='query',
                required=True,
                description="Уникальный номер инцидента для удаления (формат: INXXXXX)",
            )
        ],
        responses={
            200: OpenApiResponse(
                description="Инцидент успешно удалён",
                examples=[
                    OpenApiExample(
                        name="Deleted",
                        value={"message": "Инцидент IN00002014 удалён успешно"},
                        summary="Подтверждение удаления"
                    )
                ]
            ),
            204: OpenApiResponse(
                description="Инцидент удалён (No Content)"
            ),
            404: OpenApiResponse(
                description="Инцидент не найден по указанному номеру",
                examples=[
                    OpenApiExample(
                        name="Not Found",
                        value={"error": "Инцидент с номером IN00002014 не найден"},
                        summary="Пример ошибки 404"
                    )
                ]
            )
        },
        tags=["Accident"]
    )


def extend_schema_create_accident():
    """Create accident."""
    return extend_schema(
        summary="Создать инцидент",
        description="Создаёт новый инцидент с обязательными полями (number, category, problem, city и др.) в body. "
                    "ID генерируется автоматически. Возвращает созданный объект. "
                    "Если данные неверны (валидация) — 400.",
        responses={
            201: AccidentGetSerializer(many=False),
            400: OpenApiResponse(
                description="Неверные данные в запросе (например, invalid number или required поле отсутствует)",
                examples=[
                    OpenApiExample(
                        name="Validation Error",
                        value={
                            "number": ["Это поле обязательно."],
                            "category": ["'invalid' is not a valid choice."]
                        },
                        summary="Пример ошибок валидации"
                    )
                ]
            )
        },
        request=AccidentGetSerializer,
        examples=[
            OpenApiExample(
                name="Request Body",
                value={
                    "number": "IN00002014(str),  уникальное",
                    "category": "ФИ-7(str)",
                    "sla": "срок ликвидации аварии(str)",
                    "datetime_open": "2025-05-12T14:36:57.530Z",
                    "datetime_close": "2025-16-08T06:36:57.530Z",
                    "problem": "Описание проблемы(str)",
                    "city": "Город(str)",
                    "address": "Адрес(str)",
                    "name": "контактные данные(str)",
                    "phone": "телефон(str)",
                    "subscriber": "абонентский номер(str), необязательное",
                    "comment": "комментарий техсаппорта(str), необязательное",
                    "decide": "решение(str), необязательное",
                    "status": "open(check, close(str))",
                    "organization": "int"
                },
                summary="Сокращённый пример body для создания"
                        " (остальные поля: name, phone и т.д. — см. схему; required отмечены)"
            )
        ],
        tags=["Accident"]
    )
