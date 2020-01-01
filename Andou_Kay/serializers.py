from rest_framework import serializers

from Andou_Kay.models import Proprietaire


class Ouestserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proprietaire
        fields = '__all__'


class idserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proprietaire
        fields = 'id'
