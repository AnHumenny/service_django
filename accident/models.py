# Create your models here.
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _


class Accident(
    models.Model):
    number = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=20, blank=True)
    sla = models.CharField(max_length=20, blank=True, null=True)
    datetime_open = models.DateTimeField(default=timezone.now)
    datetime_close = models.DateTimeField(default=timezone.now, blank=True, null=True)
    problem = HTMLField()
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    subscriber = models.CharField(max_length=13)
    comment = HTMLField(blank=True)
    decide = HTMLField(blank=True)
    STATUS_CHOICES = (
        ('open', _('Open')),
        ('check', _('Check')),
        ('close', _('Close')),
    )
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"Инцидент {self.number}, {self.city}, {self.address}"

    class Meta:
        verbose_name_plural = "Accidents"