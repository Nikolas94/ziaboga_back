# Serializers define the API representation.
from rest_framework import serializers

from data_manager.models import Erabiltzailea, Egutegia, GremErab, Taldea, ErabPunt


class ErabiltzaileaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Erabiltzailea
        fields = '__all__'


class EgutegiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Egutegia
        fields = '__all__'

class GlobalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ErabPunt
        fields = '__all__'

class TaldeakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Taldea
        fields = '__all__'