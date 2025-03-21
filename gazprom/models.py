# Create your models here.
from django.db import models
from tinymce.models import HTMLField


class Gazprom(models.Model):
    ip = models.CharField(max_length=14)
    number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=30)
    region = models.CharField(max_length=255)
    comment = HTMLField()
    geo = models.CharField(max_length=50)

    def __str__(self):
        return self.geo

    class Meta:
        verbose_name_plural = "Gazproms"
