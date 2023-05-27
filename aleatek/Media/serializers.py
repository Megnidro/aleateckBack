from .models import Media
from rest_framework.serializers import ModelSerializer

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

