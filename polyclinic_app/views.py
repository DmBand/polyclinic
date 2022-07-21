from django.shortcuts import render, redirect

from .models import Region, City
from .services import city_search


def index_view(request):
    """ Главная страница """
    regions = Region.objects.values('name', 'slug')
    context = {
        'title': 'Поликлиники Беларуси',
        'regions': regions,
    }
    if request.method == 'POST':
        city = city_search(request=request)
        if city:
            return redirect('polyclinic_app:polyclinic', slug_url=city.slug)
    return render(request, 'polyclinic_app/index.html', context)


def city_view(request, slug_url):
    """ Страница выбора города """
    region = Region.objects.get(slug=slug_url)
    cities = region.city_set.all().order_by('name')
    context = {
        'title': region.name,
        'cities': cities
    }
    if request.method == 'POST':
        city = city_search(request=request)
        if city:
            return redirect('polyclinic_app:polyclinic', slug_url=city.slug)
    return render(request, 'polyclinic_app/city.html', context)


def polyclinic_view(request, slug_url):
    """ Страница выбора поликлиники """
    city = City.objects.get(slug=slug_url)
    polyclinics = city.polyclinic_set.all()
    context = {
        'title': f'Поликлиники: {city.name}',
        'polyclinics': polyclinics,
        'phone_code': city.phone_code
    }
    if request.method == 'POST':
        city = city_search(request=request)
        if city:
            return redirect('polyclinic_app:polyclinic', slug_url=city.slug)
    return render(request, 'polyclinic_app/polyclinic.html', context)
