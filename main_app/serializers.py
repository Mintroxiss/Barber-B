from rest_framework import serializers
from .models import WomanService, ManService, KidService


class WomanServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomanService
        fields = '__all__'


class ManServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManService
        fields = '__all__'


class KidServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KidService
        fields = '__all__'



