from django.contrib import messages
from django.shortcuts import redirect

from polyclinic_app.models import City


def searching_city(request):
    """ Поиск города в БД """
    get_city = request.POST.get('city')
    if get_city:
        exists = City.objects.filter(city_name__iexact=get_city.title()).exists()
        if exists:
            city = City.objects.get(city_name=get_city.title())
            return city


def redirect_polycinic(request):
    """
    Редирект на страницу поликлиник найденного города
    или выдача сообщения, что поиск не дал результатов,
    если город не был найден
    """
    city = searching_city(request=request)
    if city:
        return redirect('polyclinic_app:polyclinic', slug_url=city.slug)
    else:
        messages.info(request, message='Поиск не дал результатов')
