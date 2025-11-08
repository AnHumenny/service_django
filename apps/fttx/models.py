from django.db import models
from django.db.models import CharField
from tinymce.models import HTMLField
from apps.utils import CharFieldValidator


class Fttx(models.Model):
    city = models.CharField(max_length=30, validators=[CharFieldValidator(30)])
    claster = models.CharField(max_length=30, validators=[CharFieldValidator(30)])
    street = models.CharField(max_length=40, validators=[CharFieldValidator(40)])
    number = models.CharField(max_length=10, validators=[CharFieldValidator(10)])
    description = HTMLField(max_length=2500, blank=True, null=True, validators=[CharFieldValidator(2500)])
    askue = CharField(max_length=100, blank=True, null=True, validators=[CharFieldValidator(100)])


    def __str__(self):
        return f"{self.city}, {self.street}, {self.number}"

    class Meta:
        verbose_name_plural = ("Детальная информация по fttx(краткое описание местоположений, "
                               "контакты ответственных лиц)")
