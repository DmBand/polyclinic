from django.shortcuts import render
from .models import *


def index_view(request):
    regions = Region.objects.values('name', 'slug')
    context = {
        'title': 'Поликлиники РБ',
        'regions': regions
    }
    return render(request, 'polyclinic_app/index.html', context)


def city_view(request, slug_url):
    region = Region.objects.get(slug=slug_url)
    cities = region.city_set.all().order_by('name')
    context = {
        'title': region.name,
        'cities': cities
    }
    return render(request, 'polyclinic_app/city.html', context)


def polyclinic_view(request, slug_url):
    city = City.objects.get(slug=slug_url)
    polyclinics = city.polyclinic_set.all()
    context = {
        'title': f'Поликлиники: {city.name}',
        'polyclinics': polyclinics
    }
    return render(request, 'polyclinic_app/polyclinic.html', context)
