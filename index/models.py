# Create your models here.
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Index(
    models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    title = models.CharField(max_length=500)
    content = HTMLField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):  # С помощью функции меняем то, как будет представлена запись в модели.
        return self.title  # Указываем, что она будет идентифицироваться с помощью своего заголовка.

    class Meta:
        verbose_name_plural = "Index_x"  # Указываем правильное написание для множественного числа слова Entry


class Material(models.Model):
    date = models.DateField(verbose_name="Дата")
    cable = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.cable}"

    class Meta:
        db_table = "_material"
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class ExpansionFttx(models.Model):
    date = models.DateField(verbose_name="Дата")
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    cable = models.IntegerField()
    connector = models.IntegerField()
    crossbox = models.IntegerField()
    plint = models.IntegerField()


    def __str__(self):
        return f"{self.date} - {self.address}"

    class Meta:
        db_table = "_expansion"
        verbose_name = "Дата"
        verbose_name_plural = "Адрес"