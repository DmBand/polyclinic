from django.shortcuts import render, redirect

from .models import Region, City
from . import drf_urls
from polyclinic import urls


def search_view(request):
    """ Поиск по городу """
    context = {
        'title': 'Результаты поиска',
        'cities': None,
    }
    get_city = request.GET.get('city')
    if get_city:
        exists = City.objects.filter(city_name__iexact=get_city.title()).exists()
        if exists:
            cities = City.objects.filter(city_name=get_city.title())
            if len(cities) > 1:
                context['cities'] = cities
            else:
                return redirect('polyclinic_app:polyclinic', slug_url=cities[0].slug)
    return render(request, 'polyclinic_app/search.html', context)


def index_view(request):
    """ Главная страница """
    regions = Region.objects.values('region', 'slug')
    context = {
        'title': 'Поликлиники Беларуси',
        'regions': regions,
    }
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
    return render(request, 'polyclinic_app/city.html', context)


def polyclinic_view(request, slug_url):
    """ Страница выбора поликлиники """
    city = City.objects.get(slug=slug_url)
    polyclinics = city.polyclinics.all()
    context = {
        'title': f'Поликлиники: {city.region}',
        'polyclinics': polyclinics,
        'phone_code': city.phone_code
    }
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
    return render(request, 'polyclinic_app/api.html', context)
