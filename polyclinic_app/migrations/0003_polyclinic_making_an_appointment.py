# Generated by Django 4.0.5 on 2022-07-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polyclinic_app', '0002_city_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='polyclinic',
            name='making_an_appointment',
            field=models.URLField(blank=True, max_length=300, verbose_name='онлайн-запись'),
        ),
    ]
