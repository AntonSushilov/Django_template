from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics


from .models import SportType, TournamentType
from .serializers import SportTypeSerializer, TournamentTypeSerializer


# TournamentType
class TournamentTypeViewSet(generics.ListCreateAPIView):
    queryset = TournamentType.objects.all()
    serializer_class = TournamentTypeSerializer


class TournamentTypeViewSett(generics.RetrieveUpdateDestroyAPIView):
    queryset = TournamentType.objects.all()
    serializer_class = TournamentTypeSerializer


# SportType
class SportTypeViewSet(generics.ListCreateAPIView):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer


class SportTypeViewSett(generics.RetrieveUpdateDestroyAPIView):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer
