from django.contrib import messages
from django.shortcuts import redirect, render

from .models import City


def city_search(request):
    """ Поиск города в БД """
    get_city = request.POST.get('city')
    exists = City.objects.filter(city_name__iexact=get_city.title()).exists()
    if exists:
        cities = City.objects.filter(city_name=get_city.title())
        if len(cities) > 1:
            context = {
                'title': 'Результаты поиска',
                'cities': cities,
            }
            return render(request, 'polyclinic_app/search.html', context)
        else:
            return redirect('polyclinic_app:polyclinic', slug_url=cities[0].slug)
    else:
        messages.info(request, 'Поиск не дал результатов...')
