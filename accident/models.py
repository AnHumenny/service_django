from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from subtable.models import SubOrganization


class AccidentStatus(models.TextChoices):
    """Enumeration for the status of a user's appeal or question request"""

    OPEN = "open", "Открыто"
    CHECK = "check", "Проверка"
    CLOSE = "close", "Закрыто"


class Accident(models.Model):
    number = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=20)
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
    organization = ForeignKey(SubOrganization, related_name="Organization", default=1, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=AccidentStatus.choices,
                              default=AccidentStatus.OPEN, null=False)

    def __str__(self):
        return f"Инцидент {self.number}, {self.city}, {self.address}, {self.status} -- ({self.organization.name}) "

    class Meta:
        verbose_name_plural = "Инциденты"
