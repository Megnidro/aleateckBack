from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Entreprise, MediaCommunications


class EntrepriseSerializer(ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'

    def validate_numero_siret(self, value):
        # Nous vérifions que la le libelle  existe
        if Entreprise.objects.filter(numero_siret=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError("l'entreprise existe déjà")
        return value


class EntrepriseDetailSerializer(ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'


class MediaEntrepriseSerializer(ModelSerializer):
    class Meta:
        model = MediaCommunications
        exclude = ['id']

    def validate_entreprise(self, value):
        # Nous vérifions que la le libelle  existe
        if Entreprise.objects.filter(entreprise=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError("Vous avez deja renseigné les medias pour l'entreprise")
        return value


class MediaEntrepriseDetailSerializer(ModelSerializer):
    class Meta:
        model = MediaCommunications
        fields = '__all__'
