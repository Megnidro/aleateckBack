from itertools import chain

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .permissions import IsAdminAuthenticated
from .serializers import ProductSerializer, FilterJoinDocumentAffalire
from .models import PlanAffaire, Produit, Affaires
from Document.models import Documents


class MultipleSerializerMixin:
    # Un mixin est une classe qui ne fonctionne pas de façon autonome
    # Elle permet d'ajouter des fonctionnalités aux classes qui les étendent

    detail_serializer_class = None

    def get_serializer_class(self):
        # Notre mixin détermine quel serializer à utiliser
        # même si elle ne sait pas ce que c'est ni comment l'utiliser
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            # Si l'action demandée est le détail alors nous retournons le serializer de détail
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProductAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Produit.objects.all()
    permission_classes = [IsAdminAuthenticated]


from .serializers import FicheAffaireSerializer


class FicheAffairesAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = FicheAffaireSerializer
    queryset = Affaires.objects.all()
    permission_classes = [IsAdminAuthenticated]


# creation plan affaire
from .serializers import PlanAffaireSerializer


class PlanAffairesAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = PlanAffaireSerializer
    queryset = PlanAffaire.objects.all()
    permission_classes = [IsAdminAuthenticated]


from .serializers import FilterJoinSeraliseresAffalirePlan


class TableauDeBordQuerysetAdminView(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = FilterJoinSeraliseresAffalirePlan
    queryset = PlanAffaire.objects.all()
    querysets = Affaires.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        produit = self.request.query_params.get('produit')
        ville = self.request.query_params.get('ville')
        province = self.request.query_params.get('province')
        departement = self.request.query_params.get('departement')
        compte_postal = self.request.query_params.get('compte_postal')

        if produit:
            queryset = queryset.filter(produit=produit)
        if ville:
            queryset = queryset.filter(ville=ville)
        if province:
            queryset = queryset.filter(province=province)
        if departement:
            queryset = queryset.filter(departement=departement)
        if compte_postal:
            queryset = queryset.filter(compte_postal=compte_postal)
        return queryset

        querysets = super().get_queryset()
        numero_affaire = self.request.query_params.get('numero_affaire')
        libelle_affaire = self.request.query_params.get('libelle_affaire')
        numero_service_en_charge = self.request.query_params.get('numero_service_en_charge')
        numero_contrat_provisoire = self.request.query_params.get('numero_contrat_provisoire')
        charge_de_affaire = self.request.query_params.get('charge_de_affaire')
        statut_affaire = self.request.query_params.get('statut_affaire')
        client = self.request.query_params.get('client')
        if numero_affaire:
            querysets = querysets.filter(numero_affaire=numero_affaire)
            if libelle_affaire:
                querysets = querysets.filter(numero_affaire=numero_affaire)
            if numero_service_en_charge:
                querysets = querysets.filter(numero_service_en_charge=numero_service_en_charge)
            if client:
                querysets = querysets.filter(client=client)
            if numero_contrat_provisoire:
                querysets = querysets.filter(numero_contrat_provisoire=numero_contrat_provisoire)
            if charge_de_affaire:
                querysets = querysets.filter(charge_de_affaire=charge_de_affaire)
            if statut_affaire:
                querysets = querysets.filter(statut_affaire=statut_affaire)
        return querysets


class FilterQuerysetAdminView(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = FilterJoinSeraliseresAffalirePlan
    queryset = PlanAffaire.objects.all()
    querysets = Affaires.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        produit = self.request.query_params.get('produit')
        ville = self.request.query_params.get('ville')
        province = self.request.query_params.get('province')
        departement = self.request.query_params.get('departement')
        compte_postal = self.request.query_params.get('compte_postal')

        if produit:
            queryset = queryset.filter(produit=produit)
        if ville:
            queryset = queryset.filter(ville=ville)
        if province:
            queryset = queryset.filter(province=province)
        if departement:
            queryset = queryset.filter(departement=departement)
        if compte_postal:
            queryset = queryset.filter(compte_postal=compte_postal)
        return queryset

        querysets = super().get_queryset()
        numero_affaire = self.request.query_params.get('numero_affaire')
        libelle_affaire = self.request.query_params.get('libelle_affaire')
        numero_service_en_charge = self.request.query_params.get('numero_service_en_charge')
        numero_contrat_provisoire = self.request.query_params.get('numero_contrat_provisoire')
        charge_de_affaire = self.request.query_params.get('charge_de_affaire')
        statut_affaire = self.request.query_params.get('statut_affaire')
        client = self.request.query_params.get('client')
        if numero_affaire:
            querysets = querysets.filter(numero_affaire=numero_affaire)
            if libelle_affaire:
                querysets = querysets.filter(numero_affaire=numero_affaire)
            if numero_service_en_charge:
                querysets = querysets.filter(numero_service_en_charge=numero_service_en_charge)
            if client:
                querysets = querysets.filter(client=client)
            if numero_contrat_provisoire:
                querysets = querysets.filter(numero_contrat_provisoire=numero_contrat_provisoire)
            if charge_de_affaire:
                querysets = querysets.filter(charge_de_affaire=charge_de_affaire)
            if statut_affaire:
                querysets = querysets.filter(statut_affaire=statut_affaire)
        return querysets





class FilterQuerysetAffaireDocumentAdminView(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = FilterJoinDocumentAffalire
    queryset = Documents.objects.all()
    querysets = Affaires.objects.all()


    def get_queryset(self):
        queryset = super().get_queryset()
        emetteur = self.request.query_params.get('emetteur')
        dossier = self.request.query_params.get('dossier')
        ouvrage = self.request.query_params.get('ouvrage')
        exam = self.request.query_params.get('exam')
        nature = self.request.query_params.get('nature')
        numero_externe = self.request.query_params.get('numero_externe')
        numero_aleatek = self.request.query_params.get('numero_aleatek')
        date_de_indice = self.request.query_params.get('date_de_indice')
        date_de_reception = self.request.query_params.get('date_de_reception')
        indice = self.request.query_params.get('indice')
        titre = self.request.query_params.get('titre')
        num_revision = self.request.query_params.get('num_revision')
        fichier_attache = self.request.query_params.get('fichier_attache')
        collaborateurs = self.request.query_params.get('collaborateurs')
        intervention_technique = self.request.query_params.get('intervention_technique')
        affectation = self.request.query_params.get('affectation')

        if emetteur:
            queryset = queryset.filter(emetteur=emetteur)
            if dossier:
                queryset = queryset.filter(dossier=dossier)
            if ouvrage:
                queryset = queryset.filter(ouvrage=ouvrage)
            if exam:
                queryset = queryset.filter(exam=exam)
            if nature:
                queryset = queryset.filter(nature=nature)
            if numero_externe:
                 queryset = queryset.filter(numero_externe=numero_externe)
            if numero_aleatek:
               queryset = queryset.filter(numero_aleatek=numero_aleatek)
            if date_de_indice:
                 queryset = queryset.filter(date_de_indice=date_de_indice)
            if date_de_reception:
                 queryset = queryset.filter(date_de_reception=date_de_reception)
            if indice:
                queryset = queryset.filter(indice=indice)
            if titre:
             queryset = queryset.filter(titre=titre)
            if num_revision:
              queryset = queryset.filter(num_revision=num_revision)
            if fichier_attache:
               queryset = queryset.filter(fichier_attache=fichier_attache)
            if collaborateurs:
              queryset = queryset.filter(collaborateurs=collaborateurs)

            if intervention_technique:
              queryset = queryset.filter(intervention_technique=intervention_technique)
            if affectation:
             queryset = queryset.filter(affectation=affectation)
        return queryset

        querysets = super().get_queryset()
        numero_affaire = self.request.query_params.get('numero_affaire')
        libelle_affaire = self.request.query_params.get('libelle_affaire')
        numero_service_en_charge = self.request.query_params.get('numero_service_en_charge')
        numero_contrat_provisoire = self.request.query_params.get('numero_contrat_provisoire')
        charge_de_affaire = self.request.query_params.get('charge_de_affaire')
        statut_affaire = self.request.query_params.get('statut_affaire')
        client = self.request.query_params.get('client')
        if numero_affaire:
            querysets = querysets.filter(numero_affaire=numero_affaire)
            if libelle_affaire:
                querysets = querysets.filter(numero_affaire=numero_affaire)
            if numero_service_en_charge:
                querysets = querysets.filter(numero_service_en_charge=numero_service_en_charge)
            if client:
                querysets = querysets.filter(client=client)
            if numero_contrat_provisoire:
                querysets = querysets.filter(numero_contrat_provisoire=numero_contrat_provisoire)
            if charge_de_affaire:
                querysets = querysets.filter(charge_de_affaire=charge_de_affaire)
            if statut_affaire:
                querysets = querysets.filter(statut_affaire=statut_affaire)
        return querysets
