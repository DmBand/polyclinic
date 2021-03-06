# Generated by Django 4.0.5 on 2022-07-25 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, verbose_name='город')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('phone_code', models.CharField(max_length=10, verbose_name='телефонный код')),
            ],
            options={
                'verbose_name': 'город',
                'verbose_name_plural': 'города',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50, verbose_name='область')),
                ('slug', models.SlugField(verbose_name='url')),
            ],
            options={
                'verbose_name': 'область',
                'verbose_name_plural': 'области',
            },
        ),
        migrations.CreateModel(
            name='Polyclinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='навание')),
                ('address', models.CharField(max_length=100, verbose_name='адрес')),
                ('website', models.URLField(blank=True, max_length=300, verbose_name='сайт')),
                ('making_an_appointment', models.URLField(max_length=300, verbose_name='онлайн-запись')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polyclinics', to='polyclinic_app.city', verbose_name='город')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'поликлиника',
                'verbose_name_plural': 'поликлиники',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='имя')),
                ('number', models.CharField(max_length=50, verbose_name='телефон')),
                ('polyclinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='polyclinic_app.polyclinic', verbose_name='поликлиника')),
            ],
            options={
                'verbose_name': 'телефон',
                'verbose_name_plural': 'телефоны',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='polyclinic_app.region', verbose_name='область'),
        ),
    ]
