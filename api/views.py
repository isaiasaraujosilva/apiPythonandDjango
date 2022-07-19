from django.shortcuts import render
from rest_framework import viewsets
from api.models import cliente
from api.serializer import ClienteSerializador

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializador


