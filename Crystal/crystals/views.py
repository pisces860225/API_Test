from django.shortcuts import render
from crystals.models import Crystal
from crystals.serializers import CrystalSerializer
from rest_framework import viewsets

# Create your views here.
class CrystalViewset(viewsets.ModelViewSet):
    queryset = Crystal.objects.all()
    serializer_class = CrystalSerializer