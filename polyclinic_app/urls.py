from django.urls import path, include
from . import views


app_name = 'polyclinic_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('region/<slug:slug_url>/', views.CityView.as_view(), name='city'),
    path('polyclinic/<slug:slug_url>/', views.PolyclinicView.as_view(), name='polyclinic'),
    path('api_documentation/', views.api_view, name='api'),
]
