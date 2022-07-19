from django.shortcuts import render
from rest_framework import viewsets
from api.models import cliente, produto, pedido
from api.serializer import ClienteSerializador, ProdutoSerializador, PedidoSerializador

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializador

class ProdutoViewSet(viewsets.ModelViewSet):

    queryset = produto.objects.all()
    serializer_class = ProdutoSerializador

class PedidoViewSet(viewsets.ModelViewSet):

    queryset = pedido.objects.all()
    serializer_class = PedidoSerializador


