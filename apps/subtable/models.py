from django.db import models
from django.db.models import CharField, TextField

from apps.utils import CharFieldValidator


class SubOrganization(models.Model):
    """List of organizations"""

    name = CharField(max_length=30, blank=False, null=False, unique=True,
                             validators=[CharFieldValidator(30)] )
    type_of_work = TextField(max_length=2000, validators=[CharFieldValidator(2000)])
    email = models.EmailField(max_length=254, unique=True, validators=[CharFieldValidator(254)])


    class Meta:
        """
        Meta options for the model.

        Defines human-readable singular and plural names for the admin interface.
        """

        verbose_name = "Организация"
        verbose_name_plural = "Название организации"

    def __str__(self):
        return self.name


class SubNameEquipment(models.Model):
    """List of equipments"""

    name_of_equipment = models.CharField(max_length=100, null=True, blank=True, validators=[CharFieldValidator(100)])

    class Meta:
        """
        Meta options for the model.

        Defines human-readable singular and plural names for the admin interface.
        """
        verbose_name = "Оборудование"
        verbose_name_plural = "Название оборудования"

    def __str__(self):
        return self.name_of_equipment or "Unnamed Equipment"


class SubTypeEquipment(models.Model):
    """List of equipments"""

    name_of_equipment = models.ForeignKey(SubNameEquipment,
                                          related_name="Equipment", default=1, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank=True, verbose_name="Email address")

    class Meta:
        """
        Meta options for the model.

        Defines human-readable singular and plural names for the admin interface.
        """
        verbose_name = "Модель оборудования"
        verbose_name_plural = "Модель оборудования"

    def __str__(self):
        return f"{self.name_of_equipment}"
