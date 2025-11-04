from django.db import models
from tinymce.models import HTMLField

from apps.utils import CharFieldValidator


class Manual(
    models.Model):
    type = models.CharField(max_length=20, validators=[CharFieldValidator(20)])
    model = models.CharField(max_length=100, validators=[CharFieldValidator(100)])
    description = HTMLField(max_length=10000, validators=[CharFieldValidator(10000)])

    def __str__(self):
        return self.model

    class Meta:
        verbose_name_plural = "Мануалы"
