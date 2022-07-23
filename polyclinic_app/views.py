from django.shortcuts import render, redirect

from .models import Region, City
from .services import city_search
from . import drf_urls
from polyclinic import urls


def index_view(request):
    """ Главная страница """
    regions = Region.objects.values('region', 'slug')
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
    cities = (
        region.cities
        .values('city_name', 'slug')
        .order_by('city_name'))
    context = {
        'title': region.region,
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
    polyclinics = (
        city.polyclinics
        .select_related('city')
        .values(
            'name',
            'address',
            'website',
            'making_an_appointment',
        )
    )
    context = {
        'title': f'Поликлиники: {city.region}',
        'polyclinics': polyclinics,
        'phone_code': city.phone_code
    }
    if request.method == 'POST':
        city = city_search(request=request)
        if city:
            return redirect('polyclinic_app:polyclinic', slug_url=city.slug)
    return render(request, 'polyclinic_app/polyclinic.html', context)


def api_view(request):
    """ Страница документации API """
    host = request.get_host()
    main_url = urls.urlpatterns[-1].pattern
    context = {
        'title': 'Документация API',
        'host': host,
        'main_url': main_url,
        'all_polyclinics_url': None,
        'one_polyclinic_url': None,
    }

    for link in drf_urls.urlpatterns:
        if link.name == 'all':
            context['all_polyclinics_url'] = str(link.pattern)
        elif link.name == 'one':
            context['one_polyclinic_url'] = str(link.pattern)[:-9]

    if request.method == 'POST':
        city = city_search(request=request)
        if city:
            return redirect('polyclinic_app:polyclinic', slug_url=city.slug)
    return render(request, 'polyclinic_app/api.html', context)
