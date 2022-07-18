import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from polyclinic_app.models import Polyclinic


# class PolyckinicModel:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address


class PolyclinicSerialazer(serializers.ModelSerializer):

    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # текущий пользователь по умолчанию при создании записи
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Polyclinic
        fields = ('city', 'name', 'address', 'phone', 'url', 'making_an_appointment')

