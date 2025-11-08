from django.db import models
from apps.utils import CharFieldValidator


class BaseStation(models.Model):
    number = models.IntegerField()
    city = models.CharField(max_length=255, validators=[CharFieldValidator(255)])
    address = models.CharField(max_length=255, validators=[CharFieldValidator(255)])
    comment = models.TextField(max_length=2500, blank=True, null=True, validators=[CharFieldValidator(2500)])


    def __str__(self):  #
        return f'БС {self.number}, регион - {self.city}, {self.address}'

    class Meta:
        verbose_name_plural = "Базовые станции"
