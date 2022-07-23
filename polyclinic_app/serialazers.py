from rest_framework import serializers

from polyclinic_app.models import Polyclinic, Region, City, PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    """ Номер телефона """

    class Meta:
        model = PhoneNumber
        fields = (
            'name',
            'number',
        )


class PolyclinicSerializer(serializers.ModelSerializer):
    """ Поликлиника (без города)"""
    phone = PhoneNumberSerializer(many=True)

    class Meta:
        model = Polyclinic
        fields = (
            'id',
            'name',
            'address',
            'phone',
            'website',
            'making_an_appointment',
        )


class CitySerializer(serializers.ModelSerializer):
    """ Город (с поликлиниками)"""
    polyclinics = PolyclinicSerializer(many=True)

    class Meta:
        model = City
        fields = (
            'city_name',
            'phone_code',
            'polyclinics',
        )


class CityWithoutPolyclinicSerializer(serializers.ModelSerializer):
    """ Город (без поклклиник)"""

    class Meta:
        model = City
        fields = (
            'city_name',
            'phone_code',
        )


class PolyclinicWithCitySerializer(serializers.ModelSerializer):
    """ Поликлиника (с городом)"""
    city = CityWithoutPolyclinicSerializer(many=False)
    phone = PhoneNumberSerializer(many=True)

    class Meta:
        model = Polyclinic
        fields = (
            'city',
            'name',
            'address',
            'phone',
            'website',
            'making_an_appointment',
        )


class RegionSerializer(serializers.ModelSerializer):
    """ Область """
    cities = CitySerializer(many=True)

    class Meta:
        model = Region
        fields = (
            'region',
            'cities',
        )
