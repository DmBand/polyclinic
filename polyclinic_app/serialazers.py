from rest_framework import serializers

from polyclinic_app.models import Polyclinic, Region, City


class PolyclinicWithCitySerializer(serializers.ModelSerializer):
    """ Одна поликлиника (с городом)"""
    city = serializers.SlugRelatedField(slug_field='city_name', read_only=True)

    class Meta:
        model = Polyclinic
        exclude = (
            'id',
            'user',
        )


class PolyclinicSerializer(serializers.ModelSerializer):
    """ Одна поликлиника (без города)"""

    class Meta:
        model = Polyclinic
        fields = (
            'id',
            'name',
            'address',
            'phone',
            'url',
            'making_an_appointment',
        )


class CitySerializer(serializers.ModelSerializer):
    """ Город """

    polyclinics = PolyclinicSerializer(many=True)

    class Meta:
        model = City
        fields = (
            'city_name',
            'polyclinics',
        )


class RegionSerializer(serializers.ModelSerializer):
    """ Область """

    city = CitySerializer(many=True)

    class Meta:
        model = Region
        fields = (
            'region',
            'city',
        )
