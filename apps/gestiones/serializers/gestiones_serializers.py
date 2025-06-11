from rest_framework import serializers
from apps.gestiones.models import Gestion

class GestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestion
        fields = '__all__'
