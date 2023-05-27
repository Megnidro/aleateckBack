from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Agence


class MarqueSerializer(ModelSerializer):
    class Meta:
        model = Agence
        fields = '__all__'

    def validate_name(self, value):
        # Nous vérifions que la le libelle  existe
        if Agence.objects.filter(name=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Cette marque existe déjà Existe déja')
        return value