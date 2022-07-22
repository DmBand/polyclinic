from django.urls import path

from . import drf_views

urlpatterns = [
    path('get_polyclinics/', drf_views.PolyclinicsAPIView.as_view(), name='all'),
    path('get_one_polyclinic/<int:pk>/', drf_views.OnePolyclinicAPIView.as_view(), name='one'),
]
