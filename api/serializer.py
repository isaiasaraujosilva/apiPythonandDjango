from dataclasses import fields
from rest_framework import serializers
from django.db.models import Sum, Min
from api.models import cliente, faturamento, produto, pedido, faturamento

    
class ClienteSerializador(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ['id','nome','sobrenome','email','telefone']
class ProdutoSerializador(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = ['id','nome_do_produto','marca','quantidade','valor_unidade']
class PedidoSerializador(serializers.ModelSerializer):
    class Meta:
        model = pedido
        #valor = 10
        fields = ['id','dados_do_pedido','produto','quantidades','dados_do_cliente','valor_do_pedido','pedido_concluido']

class faturamentoSerializador(serializers.ModelSerializer):
    class Meta:
        model = faturamento
        fields = ['faturamento_total']