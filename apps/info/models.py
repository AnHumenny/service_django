from django.db import models
from django.utils import timezone

from apps.subtable.models import SubOrganization
from apps.utils import CharFieldValidator, IntegerFieldValidator


class Info(models.Model):
    """information"""
    reestr = models.IntegerField()
    date_created = models.DateField(default=timezone.now)
    city = models.CharField(max_length=20, validators=[CharFieldValidator(20)])
    street = models.CharField(max_length=30, validators=[CharFieldValidator(255)])
    home = models.CharField(max_length=7, validators=[CharFieldValidator(7)])
    apartment = models.CharField(max_length=4, validators=[CharFieldValidator(4)])
    name = models.CharField(max_length=100, validators=[CharFieldValidator(100)])
    cable_1 = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(4)])
    cable_2 = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(4)])
    cable_3 = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(4)])
    connector = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(2)])
    organization = models.ForeignKey(
        SubOrganization,
        on_delete=models.CASCADE,
        related_name="infos",
        default=2,
    )


    def __str__(self):
        return f"{self.city}, {self.street}, {self.home}, {self.apartment}"

    class Meta:
        verbose_name_plural = "Пользовательская информация"
