# Generated by Django 4.0.5 on 2022-07-22 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polyclinic_app', '0003_rename_url_polyclinic_site_alter_city_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polyclinic',
            old_name='site',
            new_name='website',
        ),
    ]