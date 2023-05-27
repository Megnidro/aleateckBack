from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import SERVICES


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = SERVICES
        fields = '__all__'

    def validate_name_code_services(self, value):
        # Nous vérifions que la le libelle  existe
        if SERVICES.objects.filter(code_services=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Ce services existe déjà Existe déja')
        return value


class ServicesDetailSerializer(ModelSerializer):
    class Meta:
        model = SERVICES
        fields = '__all__'
