from datetime import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from url_filter.backends.django import DjangoFilterBackend

from .models import Collaborateurs
from .permissions import IsAdminAuthenticated
from .serializers import ColaboratteursSerializer
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


class CollaborateursAdminViewsetAdmin(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ColaboratteursSerializer
    queryset = Collaborateurs.objects.all()
    permission_classes = [IsAdminAuthenticated]



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session


class UtilisateursConnectes(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ColaboratteursSerializer
    permission_classes = [IsAdminAuthenticated]

    def get(self, request):
        active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
        user_id_list = [session.get_decoded().get('_auth_user_id') for session in active_sessions]
        connected_users = Collaborateurs.objects.filter(id__in=user_id_list)
        username_list = [Collaborateurs.username for user in connected_users]
        return Response(username_list)

    def get_queryset(self):
        return Collaborateurs.objects.filter(is_active=True)
