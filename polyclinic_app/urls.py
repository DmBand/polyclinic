from django.urls import path
from .views import *


app_name = 'polyclinic_app'

urlpatterns = [
    path('', index_view, name='index')
]
