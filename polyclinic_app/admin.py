from django.contrib import admin
from .models import Region, City, PhoneNumber, Polyclinic


class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('region',)}
    list_display = (
        'region',
        'slug'
    )


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('city_name',)}
    list_display = (
        'city_name',
        'region'
    )


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = (
        'polyclinic',
        'title',
        'number',
    )
    list_display_links = (
        'title',
        'number'
    )
    list_filter = (
        'polyclinic',
    )


class PolyclinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'city',)
    list_filter = (
        'city',
    )


admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(Polyclinic, PolyclinicAdmin)
