from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Index(
    models.Model):
    title = models.CharField(max_length=500)
    content = HTMLField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Index_x"
