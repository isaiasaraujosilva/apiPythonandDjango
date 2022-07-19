from django.db import models
from django.db.models import Sum, Min
# Create your models here.
    


class cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome

class produto(models.Model):
    nome_do_produto = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    valor_unidade = models.FloatField()

    

    def __str__(self):
        return self.nome_do_produto

class pedido(models.Model):
    dados_do_pedido = models.CharField(max_length=30) 
    produto = models.ManyToManyField(produto)
    quantidades = models.IntegerField()
    dados_do_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    pedido_concluido = models.CharField(max_length=30)


    @property
    def valor_do_pedido(self):
        total = 0
        for produto in self.produto.all():
            total += produto.valor_unidade
            return total
        valor_do_pedido = valor_do_pedido
    
    def __str__(self):
        return self.dados_do_pedido
class faturamento(models.Model):
    
   






            


    

