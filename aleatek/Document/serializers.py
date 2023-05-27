from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Avis, Documents, FichierAttache, IntervenantInterventionDocument


class AvisSerialiser(ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'


class DocumentSerializers(ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class FichierSerializers(ModelSerializer):
    class Meta:
        model = FichierAttache
        fields = '__all__'


class IntervenantDocumentSerializer(ModelSerializer):
    class Meta:
        model = IntervenantInterventionDocument
        fields = '__all__'