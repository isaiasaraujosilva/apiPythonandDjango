from dataclasses import fields
from rest_framework import serializers
from api.models import cliente
    
class ClienteSerializador(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ['id','nome','sobrenome','email','telefone']