from django.urls import path, include
from rest_framework import routers

from .drf_views import *

router = routers.SimpleRouter()
router.register('polyclinics', PolyclinicViewSet, basename='polyclinic')

urlpatterns = [
    path('', include(router.urls))
]
