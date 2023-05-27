from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import StatutSaisiRapport, AIE, RapportConception, RapportDeVisite


class StatutSaisiRapportSerializer(ModelSerializer):
    class Meta:
        model = StatutSaisiRapport
        fields = '__all__'


class AIESerializer(ModelSerializer):
    class Meta:
        model = AIE
        fields = '__all__'


class RapportDeConceptionSerializer(ModelSerializer):
    class Meta:
        model = RapportConception
        fields = '__all__'




class RapportDeVisiteSerializer(ModelSerializer):
    class Meta:
        model = RapportDeVisite
        fields = '__all__'


