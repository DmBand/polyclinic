# Generated by Django 4.0.5 on 2022-07-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polyclinic_app', '0005_alter_polyclinic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='phone_code',
            field=models.CharField(default='+375152', max_length=10, verbose_name='телефонный код'),
            preserve_default=False,
        ),
    ]