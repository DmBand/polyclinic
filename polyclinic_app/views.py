from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {'title': 'Поликлиники РБ'}
    return render(request, 'polyclinic_app/index.html', context)


def brest_region_view(request):
    pass


def vitebsk_region_view(request):
    pass


def grodno_region_view(request):
    context = {'title': 'Гродненская область'}
    return render(request, 'polyclinic_app/grodno_region.html', context)


def gomel_region_view(request):
    pass


def minsk_region_view(request):
    pass


def mogilev_region_view(request):
    pass
