from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from subtable.models import SubOrganization


class Area(models.Model):
    city = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.city


class AccidentStatus(models.TextChoices):
    OPEN = "open", "Открыто"
    CHECK = "check", "Проверка"
    CLOSE = "close", "Закрыто"


class AccidentCategory(models.TextChoices):
    FI_1 = "Фиксированный интернет-1", "Фиксированный интернет-1"
    FI_2 = "Фиксированный интернет-2", "Фиксированный интернет-2"
    FI_3 = "Фиксированный интернет-3", "Фиксированный интернет-3"
    FI_4 = "Фиксированный интернет-4", "Фиксированный интернет-4"
    FI_7 = "Фиксированный интернет-7", "Фиксированный интернет-7"
    UI_5 = "Юридические лица-5", "Юридические лица-5"
    UI_6 = "Юридические лица-6", "Юридические лица-6"
    ID_1 = "Интернет для дома-1", "Интернет для дома-1"
    ID_2 = "Интернет для дома-2", "Интернет для дома-2"
    OW_3 = "Общественный WiFi-3", "Общественный WiFi-3"
    OW_4 = "Общественный WiFi-4", "Общественный WiFi-4"
    OW_5 = "Общественный WiFi-5", "Общественный WiFi-5"
    OW_6 = "Общественный WiFi-6", "Общественный WiFi-6"


class Accident(models.Model):
    number = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=50, choices=AccidentCategory.choices)
    sla = models.CharField(max_length=20)
    datetime_open = models.DateTimeField(default=timezone.now)
    datetime_close = models.DateTimeField(default=timezone.now)
    problem = HTMLField(max_length=2500)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    subscriber = models.CharField(max_length=13)
    comment = HTMLField(max_length=2500, null=True, blank=True)
    decide = HTMLField(max_length=2500, null=True, blank=True)
    organization = models.ForeignKey(SubOrganization, related_name="Organization", default=1, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=AccidentStatus.choices,
                              default=AccidentStatus.OPEN, null=False)

    def __str__(self):
        return f"Инцидент {self.number}, {self.city}, {self.address}, {self.status} -- ({self.organization.name})"

    class Meta:
        verbose_name_plural = "Инциденты"


