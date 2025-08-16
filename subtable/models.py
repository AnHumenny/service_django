from django.db import models
from django.db.models import CharField, TextField


class SubOrganization(models.Model):
    """List of organizations"""

    name = CharField(max_length=30, blank=False, null=False, unique=True )
    type_of_work = TextField(max_length=2000, blank=False, null=False)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)


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

    name_of_equipment = models.CharField(max_length=100, blank=True, null=True)

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
    type_of_equipment = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        """
        Meta options for the model.

        Defines human-readable singular and plural names for the admin interface.
        """
        verbose_name = "Модель оборудования"
        verbose_name_plural = "Модель оборудования"

    def __str__(self):
        return f"{self.name_of_equipment} - {self.type_of_equipment}"
