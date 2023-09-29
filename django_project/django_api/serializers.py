from rest_framework import serializers
from .models import PVE

class PVESerializer(serializers.ModelSerializer):

    class Meta:
        model = PVE
        fields = ('id', 'title', 'lvlMax', 'currentLvl', 'exp')
