from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Polyclinic, City
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serialazers import PolyclinicSerialazer


class PolyclinicViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = Polyclinic.objects.all()
    serializer_class = PolyclinicSerialazer

    # permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Polyclinic.objects.all()
        return Polyclinic.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)  # False - возвр список, True - одну запись
    def city(self, request, pk=None):
        city = City.objects.get(pk=pk)
        return Response({'cities': city.name})

    @action(methods=['get'], detail=False)  # False - возвр список, True - одну запись
    def cities(self, request):
        city = City.objects.all()
        return Response({'cities': [c.name for c in city]})
