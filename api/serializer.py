from dataclasses import fields
from rest_framework import serializers
from api.models import cliente, produto
    
class ClienteSerializador(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ['id','nome','sobrenome','email','telefone']
class ProdutoSerializador(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = ['id','nome_do_produto','marca','unidade']