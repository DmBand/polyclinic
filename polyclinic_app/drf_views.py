from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Polyclinic, Region
from .serialazers import RegionSerializer, PolyclinicWithCitySerializer
from .permissions import IsAdminOrReadOnly


class PolyclinicsAPIView(APIView):
    """ Получение всех поликлиник в разрезе областей и городов """
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        region = Region.objects.all()
        serialazer = RegionSerializer(region, many=True)
        return Response(serialazer.data)


class OnePolyclinicAPIView(APIView):
    """ Получение одной поликлиники """
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        polyclinic = Polyclinic.objects.get(pk=pk)
        serializer = PolyclinicWithCitySerializer(polyclinic)
        return Response(serializer.data)
