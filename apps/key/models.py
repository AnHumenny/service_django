from django.db import models

from apps.utils import IntegerFieldValidator, CharFieldValidator


class Key(models.Model):
    city = models.CharField(max_length=20, validators=[CharFieldValidator(20)])
    street = models.CharField(max_length=30, validators=[CharFieldValidator(30)])
    home = models.CharField(max_length=7, validators=[CharFieldValidator(2)])
    entrance = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(2)])
    ind = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(2)])
    stand = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(2)])


    def __str__(self):
        return f"{self.city}, {self.street}, {self.home}"

    class Meta:
        verbose_name_plural = "Таблица ключей по оборудованию"
