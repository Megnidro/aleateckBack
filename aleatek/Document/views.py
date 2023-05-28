from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from url_filter.backends.django import DjangoFilterBackend

from .models import Avis, Documents, FichierAttache, IntervenantInterventionDocument, Commentaire
from .permissions import IsAdminAuthenticated
from .serializers import AvisSerialiser, DocumentSerializers, FichierSerializers, IntervenantDocumentSerializer
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


class AvisAdminViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = AvisSerialiser
    queryset = Avis.objects.all()
    permission_classes = [IsAdminAuthenticated]


class DocumentsAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = DocumentSerializers
    queryset = Documents.objects.all()
    permission_classes = [IsAdminAuthenticated]


class FichierAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = FichierSerializers
    queryset = FichierAttache.objects.all()
    permission_classes = [IsAdminAuthenticated]

class AffectaionInterventionAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = IntervenantDocumentSerializer
    queryset = IntervenantInterventionDocument.objects.all()
    permission_classes = [IsAdminAuthenticated]


from .serializers import CommentaireSerializer
class CommentaireAvisAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = CommentaireSerializer
    queryset = Commentaire.objects.all()
    permission_classes = [IsAdminAuthenticated]
