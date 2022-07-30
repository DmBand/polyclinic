from django.contrib import messages
from django.shortcuts import redirect, render

from polyclinic_app.models import City


def searching_city(request):
    """ Поиск города в БД """
    get_city = request.POST.get('city')
    if get_city:
        if City.objects.filter(city_name__iexact=get_city.title()).exists():
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


class POSTMixin:
    """ Реализация метода POST """

    def post(self, request, **kwargs):
        searching_result = redirect_polycinic(request=request)
        if searching_result:
            return searching_result

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
