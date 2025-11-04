from django.db import models
from django.db.models import ForeignKey

from apps.accident.models import Area
from apps.subtable.models import SubOrganization
from apps.utils import IntegerFieldValidator, CharFieldValidator


class Material(models.Model):
    date = models.DateField(verbose_name="Дата")
    city = models.ForeignKey(Area, related_name="сity", default=1, on_delete=models.CASCADE)
    cable = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    connector = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    crossbox = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(2)])
    plint = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    vols = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(5)])
    mediaconverter = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(2)])
    sfp = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    electrical_tape = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    screeds = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    corrugation = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    bracket = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    organization = ForeignKey(SubOrganization, blank=True,
                              related_name="city_organization", default=2, on_delete=models.CASCADE)

    def __str__(self):
        return f"Приход на {self.date} " #--- {self.organization.name}"

    class Meta:
        db_table = "_material"
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class ExpansionFttx(models.Model):
    date = models.DateField(verbose_name="Дата")
    city = models.CharField(max_length=50, null=True, blank=True, validators=[CharFieldValidator(50)])
    street = models.CharField(max_length=50, null=True, blank=True, validators=[CharFieldValidator(50)])
    home = models.CharField(max_length=10, null=True, blank=True, validators=[CharFieldValidator(10)])
    entrance = models.IntegerField(null=True, blank=True, validators=[IntegerFieldValidator(3)])
    floor = models.IntegerField(null=True, blank=True, validators=[IntegerFieldValidator(3)])
    cable = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    connector = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    crossbox = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(2)])
    plint = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    type_of_switch = models.CharField(max_length=50, null=True, blank=True, validators=[CharFieldValidator(50)])
    quantity_of_switch = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    organization = ForeignKey(SubOrganization, related_name="fttx_organization", default=2, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} -- г. {self.city}, ул. {self.street}, д. {self.home} --- {self.organization.name} "

    class Meta:
        db_table = "_expansion"
        verbose_name = "Расширение fttx"
        verbose_name_plural = "Расширение fttx "


class ExpansionWTTX(models.Model):
    date = models.DateField(verbose_name="Дата")
    city = models.CharField(max_length=50, null=True, blank=True, validators=[CharFieldValidator(50)])
    address = models.CharField(max_length=255, null=True, blank=True, validators=[CharFieldValidator(255)])
    cable = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    connector = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    type_of_switch = models.CharField(max_length=50, null=True, blank=True, validators=[CharFieldValidator(50)])
    quantity_of_switch = models.IntegerField(blank=True,
                                             null=True, validators=[IntegerFieldValidator(3)])
    type_of_wifi = models.CharField(max_length=50, null=True, blank=True, validators=[CharFieldValidator(50)])
    quantity_of_wifi = models.IntegerField(blank=True,
                                             null=True, validators=[IntegerFieldValidator(3)])
    organization = ForeignKey(SubOrganization, related_name="wttx_organization", default=2, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.address} --- {self.organization.name}"

    class Meta:
        db_table = "_expansion_WTTX"
        verbose_name = "Монтаж WTTX"
        verbose_name_plural = "Монтаж WTTX"


class ChangeEquipment(models.Model):
    date = models.DateField(verbose_name="Дата")
    number = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=50, null=True, blank=True, validators=[CharFieldValidator(50)])
    street = models.CharField(null=True, blank=True, max_length=50, validators=[CharFieldValidator(50)])
    home = models.CharField(null=True, blank=True, max_length=8, validators=[CharFieldValidator(8)])
    entrance = models.IntegerField(blank=True, null=True, validators=[IntegerFieldValidator(3)])
    type_of_equipment = models.CharField(max_length=50, null=True, blank=True, validators=[CharFieldValidator(50)])
    quantity_of_equipment = models.IntegerField(blank=True, null=True,
                                                validators=[IntegerFieldValidator(3)])
    describe = models.TextField(null=True, blank=True, max_length=2500, validators=[CharFieldValidator(2500)])
    mac_address = models.CharField(null=True, blank=True, max_length=50, validators=[CharFieldValidator(50)])
    serial_number = models.CharField(null=True, blank=True, max_length=50, validators=[CharFieldValidator(50)])
    organization = ForeignKey(SubOrganization, related_name="equipment_organization",
                              default=2, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.date} - {self.city} - {self.street} - {self.home} - {self.entrance} - {self.type_of_equipment}"
                f"---{self.organization.name}")

    class Meta:
        db_table = "_change_equipment"
        verbose_name = "Замена оборудования"
        verbose_name_plural = "Замена оборудования"
