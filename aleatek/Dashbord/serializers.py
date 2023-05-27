from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import PlanAffaire, Produit, Affaires
from Document.models import Documents


# plan affaires creation


class FicheAffaireSerializer(ModelSerializer):
    class Meta:
        model = Affaires
        fields = '__all__'


class PlanAffaireSerializer(ModelSerializer):
    class Meta:
        model = PlanAffaire
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'


class FilterJoinSeraliseresAffalirePlan(ModelSerializer):
    affaires = serializers.SerializerMethodField()

    class Meta:
        model = PlanAffaire
        fields = ['affaires', 'id', 'libelle_plan_affaire', 'numero_plan', 'risque', 'devise', 'destination',
                  'debut_chantier', 'delai_des_travaux', 'fin_chantier', 'visite_reunions', 'cplt_geo',
                  'numero_voie', 'lieu_dit', 'compte_postal', 'ville', 'pays', 'departement', 'province',
                  'type_affaire', 'produit', 'montant_des_travaux', 'type_montant', 'debut_prestation_bv',
                  'nb', 'intervention_technique', 'missions', 'constructeurs']

    def get_affaires(self, obj):
        queryset = obj.affaire
        serializer = FicheAffaireSerializer(queryset).data
        return serializer




class FilterJoinDocumentAffalire(ModelSerializer):
    affaires = serializers.SerializerMethodField()

    class Meta:
        model = Documents
        fields = ['affaires', 'emetteur', 'dossier', 'ouvrage', 'exam', 'nature', 'numero_externe', 'numero_aleatek',
                  'date_de_indice', 'date_de_reception', 'indice', 'titre', 'num_revision', 'fichier_attache',
                  'collaborateurs', 'intervention_technique', 'affectation']
    def get_affaires(self, obj):
        queryset = obj.affaire
        serializer = FicheAffaireSerializer(queryset).data
        return serializer
