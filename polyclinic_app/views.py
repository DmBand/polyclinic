from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import *


def index_view(request):
    regions = Region.objects.values('name', 'slug')
    context = {
        'title': 'Поликлиники РБ',
        'regions': regions,
    }
    if request.method == 'POST':
        get_city = request.POST.get('city')
        exists = City.objects.filter(name__iexact=get_city.title()).exists()
        if exists:
            city = City.objects.get(name=get_city.title())
            return redirect('polyclinic_app:polyclinic', slug_url=city.slug)
        else:
            messages.info(request, 'Поиск не дал результатов...')
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
        'polyclinics': polyclinics,
        'phone_code': city.phone_code
    }
    return render(request, 'polyclinic_app/polyclinic.html', context)


