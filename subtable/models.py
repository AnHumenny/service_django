from django.db import models
from django.db.models import CharField, TextField


class SubOrganization(models.Model):
    name = CharField(max_length=30, blank=False, null=False, unique=True )
    type_of_work = TextField(max_length=2000, blank=False, null=False)

    class Meta:
        """
        Meta options for the model.

        Defines human-readable singular and plural names for the admin interface.
        """

        verbose_name = "Organization"
        verbose_name_plural = "List of organization"


    def __str__(self):
        return self.name