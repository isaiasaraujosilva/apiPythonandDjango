from django.db import models

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
    unidade = models.IntegerField()
    valor_unidade = models.FloatField()
    

    def __str__(self):
        return self.nome_do_produto

class pedido(models.Model):
    dados_do_pedido = models.CharField(max_length=30) 
    produto = models.ForeignKey(produto, on_delete=models.CASCADE)
    quantidades = models.IntegerField()
    dados_do_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.dados_do_pedido