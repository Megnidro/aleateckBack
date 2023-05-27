from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . models import ASO


class DestinationSerializer(ModelSerializer):
    class Meta:
        model = ASO
        fields = '__all__'
