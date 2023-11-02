from django.db.models import fields
from rest_framework import serializers

from .models import SportType, TournamentType

class TournamentTypeSerializer(serializers.ModelSerializer):
    # achievement_name = serializers.CharField(source='name')
    title = serializers.CharField(max_length=64)
    description = serializers.CharField()

    class Meta:
        model = TournamentType
        # fields = ('id', 'title', 'description')
        fields = '__all__'

class SportTypeSerializer(serializers.ModelSerializer):
    # achievement_name = serializers.CharField(source='name')
    title = serializers.CharField(max_length=64)
    description = serializers.CharField()

    class Meta:
        model = SportType
        # fields = ('id', 'title', 'description')
        fields = '__all__'
