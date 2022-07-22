from django.contrib.auth.models import User
from django.db import models


class Region(models.Model):
    """ Область """
    region = models.CharField(
        max_length=50,
        verbose_name='область',
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='url',
    )

    class Meta:
        verbose_name = 'область'
        verbose_name_plural = 'области'

    def __str__(self):
        return self.region


class City(models.Model):
    """ Город """
    city_name = models.CharField(
        max_length=50,
        verbose_name='город',
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='url',
    )
    phone_code = models.CharField(
        max_length=10,
        verbose_name='телефонный код',
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        verbose_name='область',
        related_name='cities',
    )

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.city_name


class Polyclinic(models.Model):
    """ Поликлиника """
    name = models.CharField(
        max_length=100,
        verbose_name='навание',
    )
    address = models.CharField(
        max_length=100,
        verbose_name='адрес',
    )
    website = models.URLField(
        max_length=300,
        verbose_name='сайт',
        blank=True,
    )
    making_an_appointment = models.URLField(
        max_length=300,
        verbose_name='онлайн-запись',
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='город',
        related_name='polyclinics',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )

    class Meta:
        verbose_name = 'поликлиника'
        verbose_name_plural = 'поликлиники'

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    """ Номер телефона """
    name = models.CharField(
        max_length=30,
        verbose_name='имя',
    )
    number = models.CharField(
        max_length=50,
        verbose_name='телефон',
    )
    polyclinic = models.ForeignKey(
        Polyclinic,
        on_delete=models.CASCADE,
        verbose_name='поликлиника',
        related_name='phone',
    )

    class Meta:
        verbose_name = 'телефон'
        verbose_name_plural = 'телефоны'

    def __str__(self):
        return self.name
