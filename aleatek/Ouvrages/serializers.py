from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Ouvrages, OuvragesDiffusion, AvisOuvrages


class OuvrageSerialiser(ModelSerializer):
    class Meta:
        model = Ouvrages
        fields = '__all__'


class OuvragesDiffusionSerializers(ModelSerializer):
    class Meta:
        model = OuvragesDiffusion
        fields = '__all__'


class AvisSurOuvragesSerializers(ModelSerializer):
    class Meta:
        model = AvisOuvrages
        fields = '__all__'

