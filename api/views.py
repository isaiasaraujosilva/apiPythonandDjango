from django.shortcuts import render
from rest_framework import viewsets
from api.models import cliente, faturamento, produto, pedido
from api.serializer import ClienteSerializador, ProdutoSerializador, PedidoSerializador, faturamentoSerializador
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
##from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializador

class ProdutoViewSet(viewsets.ModelViewSet):

    queryset = produto.objects.all()
    serializer_class = ProdutoSerializador

class PedidoViewSet(viewsets.ModelViewSet):

    #queryset = pedido.objects.all()
    serializer_class = PedidoSerializador
    
    # pedidos por cliente
    def get_queryset(self):
        queryset = pedido.objects.all()
        cliente = self.request.query_params.get('cliente')

        if cliente:
            queryset = queryset.filter(dados_do_cliente=cliente)
        return queryset

class faturamentoViewSet(viewsets.ModelViewSet):
    queryset = faturamento.objects.all()
    serializer_class = faturamentoSerializador

