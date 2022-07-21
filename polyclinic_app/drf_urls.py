from django.urls import path, include
from rest_framework import routers

from .drf_views import PolyclinicsAPIView

# router = routers.SimpleRouter()
# router.register('polyclinics', PolyclinicViewSet, basename='polyclinic')

urlpatterns = [
    path('get_polyclinics/', PolyclinicsAPIView.as_view())
    # path('', include(router.urls))
]
