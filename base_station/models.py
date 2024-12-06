# Create your models here.
from django.db import models
from django.utils import timezone


class BaseStation(
    models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    number = models.IntegerField()
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)


    def __str__(self):  # С помощью функции меняем то, как будет представлена запись в модели.
        return self.city   # Указываем, что она будет идентифицироваться с помощью своего заголовка.

    class Meta:
        verbose_name_plural = "BaseStations"  # Указываем правильное написание для множественного числа слова Entry