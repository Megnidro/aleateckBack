from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import PlanAffaireCreation


class PlanAffaireSerializer(ModelSerializer):
    class Meta:
        model = PlanAffaireCreation
        exclude = ['id']

    def validate_libelle_affaire(self, value):
        # Nous vérifions que la le libelle  existe
        if PlanAffaireCreation.objects.filter(libelle_affaire=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Cet Affaire existe déjà Existe déja')
        return value


class PlanDetailSerializer(ModelSerializer):
    class Meta:
        model = PlanAffaireCreation
        fields = '__all__'
