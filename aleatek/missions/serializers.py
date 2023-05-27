from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Missions


class MissionsSerializer(ModelSerializer):
    class Meta:
        model = Missions
        fields = '__all__'

