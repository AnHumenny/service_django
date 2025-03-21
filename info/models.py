# Create your models here.
from django.db import models
from django.utils import timezone


class Info(models.Model):
    reestr = models.IntegerField()
    date_created = models.DateField(default=timezone.now)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    home = models.CharField(max_length=7)
    apartment = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    cable_1 = models.IntegerField()
    cable_2 = models.IntegerField()
    cable_3 = models.IntegerField()
    connector = models.IntegerField()


    def __str__(self):
        return f"{self.city}, {self.street}, {self.home}, {self.apartment}"

    class Meta:
        verbose_name_plural = "Info_s"
