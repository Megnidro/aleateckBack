from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Media
from .permissions import IsAdminAuthenticated

# Create your views here.

from .serializers import MediaSerializer


class MediaSerializerAdmin(ModelViewSet):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        charg_affaire_id = self.kwargs['charg_affaire_id']
        return Media.objects.filter(charg_affaire_id=charg_affaire_id)

