from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

from apps.utils import CharFieldValidator


class Index( models.Model):
    title = models.CharField(max_length=500, validators=[CharFieldValidator(500)])
    content = HTMLField(max_length=5000, validators=[CharFieldValidator(5000)])
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Краткие сводки"
