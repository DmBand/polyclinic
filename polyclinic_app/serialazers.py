from rest_framework import serializers

from polyclinic_app.models import Polyclinic, Region, City


class PolyclinicSerializer(serializers.ModelSerializer):
    """ Одна поликлиника (без города)"""

    class Meta:
        model = Polyclinic
        fields = (
            'name',
            'address',
            'phone',
            'url',
            'making_an_appointment',
        )


class CitySerializer(serializers.ModelSerializer):
    """ Город """

    polyclinic = PolyclinicSerializer(many=True)

    class Meta:
        model = City
        fields = (
            'name',
            'polyclinic',
        )


class RegionSerializer(serializers.ModelSerializer):
    """ Область """

    city = CitySerializer(many=True)

    class Meta:
        model = Region
        fields = (
            'name',
            'city',
        )
