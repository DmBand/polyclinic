from django.contrib.auth.models import User
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name='область')
    slug = models.SlugField(max_length=50, verbose_name='url')

    class Meta:
        verbose_name = 'область'
        verbose_name_plural = 'области'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='город')
    slug = models.SlugField(max_length=50, verbose_name='url')
    phone_code = models.CharField(max_length=10, verbose_name='телефонный код')
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, verbose_name='область', related_name='city'
    )

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.name


class Polyclinic(models.Model):
    name = models.CharField(max_length=100, verbose_name='навание')
    address = models.CharField(max_length=100, verbose_name='адрес')
    phone = models.CharField(max_length=50, verbose_name='телефон регистратуры')
    url = models.URLField(max_length=300, verbose_name='сайт', blank=True)
    making_an_appointment = models.URLField(max_length=300, verbose_name='онлайн-запись')
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name='город', related_name='polyclinic'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    class Meta:
        verbose_name = 'поликлиника'
        verbose_name_plural = 'поликлиники'

    def __str__(self):
        return self.name
