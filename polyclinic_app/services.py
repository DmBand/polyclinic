from django.contrib import messages

from .models import City


def city_search(request):
    """ Поиск города в БД """
    get_city = request.POST.get('city')
    exists = City.objects.filter(city_name__iexact=get_city.title()).exists()
    if exists:
        city = City.objects.get(city_name=get_city.title())
        return city
    else:
        messages.info(request, 'Поиск не дал результатов...')
