from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Region, City, Polyclinic
from . import drf_urls
from polyclinic import urls, settings
from .services import redirect_polycinic


class IndexView(ListView):
    """ Главная страница """
    template_name = 'polyclinic_app/index.html'
    context_object_name = 'regions'
    queryset = Region.objects.values('region', 'slug')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Поликлиники Беларуси'
        return context

    def post(self, request, **kwargs):
        searching_result = redirect_polycinic(request=request)
        if searching_result:
            return searching_result

        context = self.get_context_data(object_list=self.queryset, **kwargs)
        return render(request, self.template_name, context)


class CityView(ListView):
    """ Страница выбора города """
    template_name = 'polyclinic_app/city.html'
    context_object_name = 'cities'

    def get_queryset(self):
        return (City.objects
                .filter(region__slug=self.kwargs['slug_url'])
                .values('city_name', 'slug'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        region = Region.objects.filter(slug=self.kwargs['slug_url']).values('region')
        context['title'] = region[0].get('region')
        return context

    def post(self, request, **kwargs):
        searching_result = redirect_polycinic(request=request)
        if searching_result:
            return searching_result

        context = self.get_context_data(object_list=self.get_queryset(), **kwargs)
        return render(request, self.template_name, context)


class PolyclinicView(ListView):
    """ Страница выбора поликлиники """
    template_name = 'polyclinic_app/polyclinic.html'
    context_object_name = 'polyclinics'

    def get_queryset(self):
        return Polyclinic.objects.filter(city__slug=self.kwargs['slug_url'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        city = City.objects.get(slug=self.kwargs['slug_url'])
        context['title'] = f'Поликлиники: {city.region}'
        context['phone_code'] = city.phone_code
        return context

    def post(self, request, **kwargs):
        searching_result = redirect_polycinic(request=request)
        if searching_result:
            return searching_result

        context = self.get_context_data(object_list=self.get_queryset(), **kwargs)
        return render(request, self.template_name, context)


class APIView(TemplateView):
    """ Страница документации API """
    template_name = 'polyclinic_app/api.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        host = self.request.get_host()
        main_url = (urls.urlpatterns[-2].pattern
                    if settings.DEBUG
                    else urls.urlpatterns[-1].pattern)
        context['title'] = 'Документация API'
        context['host'] = host
        context['main_url'] = main_url
        context['all_polyclinics_url'] = None
        context['one_polyclinic_url'] = None

        for link in drf_urls.urlpatterns:
            if link.name == 'all':
                context['all_polyclinics_url'] = str(link.pattern)
            elif link.name == 'one':
                context['one_polyclinic_url'] = str(link.pattern)[:-9]

        return context

    def post(self, request, **kwargs):
        searching_result = redirect_polycinic(request=request)
        if searching_result:
            return searching_result

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
