from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import InterventionTechniqueAssocie, PrestatationAssocie


class InterventionTechniqueSerializer(ModelSerializer):
    class Meta:
        model = InterventionTechniqueAssocie
        fields = '__all__'

    def validate_name_code_libelle(self, value):
        # Nous vérifions que la le libelle  existe
        if InterventionTechniqueAssocie.objects.filter(code_libelle=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Cette IT  existe déjà Existe déja ou est en cours ')
        return value



class PrestationAssocieIT(ModelSerializer):
    class Meta:
        model = PrestatationAssocie
        fields = '__all__'

