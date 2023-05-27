from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . models import Destination


class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

    def validate_name(self, value):
        # Nous vérifions que la le libelle  existe
        if Destination.objects.filter(name=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError("l'entreprise existe déjà")
        return value

