import email
from datetime import timezone
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from url_filter.backends.django import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Collaborateurs
from .permissions import IsAdminAuthenticated
from .serializers import ColaboratteursSerializer
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import *


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

from datetime import *
from django.utils import timezone
from datetime import datetime
from django.contrib.sessions.models import Session
class UtilisateursConnectes(MultipleSerializerMixin, ModelViewSet, LoginRequiredSuperuserMixim):
    serializer_class = ColaboratteursSerializer

    def retrieve(self, request, pk=None):
        active_sessions = Session.objects.filter(expire_date__gte=datetime.now())
        user_id_list = [session.get_decoded().get('_auth_user_id') for session in active_sessions]
        connected_user = Collaborateurs.objects.filter(id__in=user_id_list, id=pk).first()

        if connected_user:
            serializer = self.serializer_class(connected_user)
            return Response(serializer.data)
        else:
            return Response({'message': 'Utilisateur non trouvé.'}, status=404)

    def get_queryset(self):
        active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
        user_id_list = [session.get_decoded().get('_auth_user_id') for session in active_sessions]
        connected_users = Collaborateurs.objects.filter(id__in=user_id_list)
        return connected_users.filter(id=self.kwargs['pk'])
