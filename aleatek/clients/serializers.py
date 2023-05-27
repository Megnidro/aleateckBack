from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate_email(self, value):
        # Nous vérifions que le  client  existe
        if Client.objects.filter(email=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Ce client existe déjà')
        return value


