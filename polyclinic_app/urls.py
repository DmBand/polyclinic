from django.urls import path
from .views import *


app_name = 'polyclinic_app'

urlpatterns = [
    path('', index_view, name='index'),
    path('city/<slug:slug_url>/', city_view, name='city'),
    path('polyclinic/<slug:slug_url>/', polyclinic_view, name='polyclinic'),
]
