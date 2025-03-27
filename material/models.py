from django.db import models
from django.utils.translation import gettext_lazy as _

from accident.models import Accident


class Material(models.Model):
    date = models.DateField(verbose_name="Дата")
    cable = models.IntegerField(default=0)
    connector = models.IntegerField(default=0)
    crossbox = models.IntegerField(default=0)
    plint = models.IntegerField(default=0)
    vols = models.IntegerField(default=0)
    mediaconverter = models.IntegerField(default=0)
    sfp = models.IntegerField(default=0)
    electrical_tape = models.IntegerField(default=0)
    screeds = models.IntegerField(default=0)
    corrugation = models.IntegerField(default=0)
    bracket = models.IntegerField(default=0)

    def __str__(self):
        return f"Приход на {self.date}"

    class Meta:
        db_table = "_material"
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class ExpansionFttx(models.Model):
    date = models.DateField(verbose_name="Дата")
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50, null=True, blank=True)
    home = models.CharField(max_length=10, null=True, blank=True)
    entrance = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    cable = models.IntegerField()
    connector = models.IntegerField()
    crossbox = models.IntegerField()
    plint = models.IntegerField()
    type_of_switch = models.CharField(max_length=50, null=True, blank=True)
    quantity_of_switch = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} -- г. {self.city}, ул. {self.street}, д. {self.home} "

    class Meta:
        db_table = "_expansion"
        verbose_name = "Расширение fttx"
        verbose_name_plural = "Расширение fttx "


class ExpansionWTTX(models.Model):
    date = models.DateField(verbose_name="Дата")
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    cable = models.IntegerField(default=0)
    connector = models.IntegerField(default=0)
    type_of_switch = models.CharField(max_length=50, null=True, blank=True)
    quantity_of_switch = models.IntegerField(default=0)
    type_of_wifi = models.CharField(max_length=50, null=True, blank=True)
    quantity_of_wifi = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} - {self.address}"

    class Meta:
        db_table = "_expansion_WTTX"
        verbose_name = "Монтаж WTTX"
        verbose_name_plural = "Монтаж WTTX"


class ChangeEquipment(models.Model):
    date = models.DateField(verbose_name="Дата")
    number = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=50)
    street = models.CharField(null=True, blank=True, max_length=50)
    home = models.CharField(null=True, blank=True, max_length=8)
    entrance = models.IntegerField(null=True, blank=True)
    type_of_equipment = models.CharField(max_length=50)
    quantity_of_equipment = models.IntegerField()
    describe = models.TextField(null=True, blank=True, max_length=2500)
    mac_address = models.CharField(null=True, blank=True, max_length=50)
    serial_number = models.CharField(null=True, blank=True, max_length=50)
    ORGANIZATION_CHOICES = (
        ("Выберите организацию", _('------')),
        ('Органиция 1', _('Органиция 1')),
        ('Органиция 1', _('Органиция 2')),
        ('Органиция 3', _('Органиция 3')),
        ('Органиция 4', _('Органиция 4')),
    )

    organization = models.CharField(max_length=50, choices=ORGANIZATION_CHOICES, default='------')

    def __str__(self):
        return f"{self.date} - {self.city} - {self.street} - {self.home} - {self.entrance} - {self.type_of_equipment}"

    class Meta:
        db_table = "_change_equipment"
        verbose_name = "Замена оборудования"
        verbose_name_plural = "Замена оборудования"



