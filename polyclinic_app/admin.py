from django.contrib import admin
from .models import *


class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'region')


class PolyclinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', )
    list_filter = ('city',)


admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Polyclinic, PolyclinicAdmin)
