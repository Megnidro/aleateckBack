from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from url_filter.backends.django import DjangoFilterBackend

from .models import Entreprise
from .permissions import IsAdminAuthenticated
from .serializers import EntrepriseSerializer, EntrepriseDetailSerializer, MediaEntrepriseSerializer, \
    MediaEntrepriseDetailSerializer
from rest_framework.decorators import action


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


class EntrepriseAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = EntrepriseSerializer
    detail_serializer_class = EntrepriseDetailSerializer
    queryset = Entreprise.objects.all()
    permission_classes = [IsAdminAuthenticated]


class MediaEntrepriseAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = MediaEntrepriseSerializer
    detail_serializer_class = MediaEntrepriseDetailSerializer
    queryset = Entreprise.objects.all()
    permission_classes = [IsAdminAuthenticated]
