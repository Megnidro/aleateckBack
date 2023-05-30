from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from url_filter.backends.django import DjangoFilterBackend
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Ouvrages, OuvragesDiffusion, AvisOuvrages
from .permissions import IsAdminAuthenticated
from .serializers import OuvrageSerialiser, OuvragesDiffusionSerializers, AvisSurOuvragesSerializers
from rest_framework.decorators import action
from rest_framework.views import APIView

from  Document.models import Documents


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


class OuvagesAdminViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = OuvrageSerialiser
    queryset = Ouvrages.objects.all()
    permission_classes = [IsAdminAuthenticated]



class AvisSurOuvragesAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = AvisSurOuvragesSerializers
    queryset = AvisOuvrages.objects.all()
    permission_classes = [IsAdminAuthenticated]


class OuvagesDiffusionAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = OuvragesDiffusionSerializers
    queryset = OuvragesDiffusion.objects.all()
    permission_classes = [IsAdminAuthenticated]

class OuvrageidAffaireid(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id_ouvrage, id_affaire):

        data = {
            'id_ouvrage' : id_ouvrage,
            'id_affaire': id_affaire
        }
        return Response(data)



class OuvrageidAffaireid(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id_ouvrage, id_affaire):
        data_document = Documents.objects.select_related('exam').filter(ouvrage=id_ouvrage)

        data = {
            'result': list(data_document)
        }
        return Response(data)


