# Create your models here.
from django.core.validators import validate_ipv4_address
from django.db import models
from tinymce.models import HTMLField

from apps.utils import CharFieldValidator


class Gazprom(models.Model):
    ip = models.CharField(max_length=14, validators=[validate_ipv4_address])
    number = models.CharField(max_length=10, validators=[CharFieldValidator(10)])
    address = models.CharField(max_length=255, validators=[CharFieldValidator(255)])
    type = models.CharField(max_length=30, validators=[CharFieldValidator(30)])
    region = models.CharField(max_length=255, validators=[CharFieldValidator(255)])
    comment = HTMLField(max_length=2500, blank=True, null=True, validators=[CharFieldValidator(2500)])
    geo = models.CharField(max_length=50, blank=True, null=True,validators=[validate_ipv4_address])

    def __str__(self):
        return f"Номер - {self.number}, регион - {self.region}, {self.address}"

    class Meta:
        verbose_name_plural = "АЗС Газпрома"
