from django.db import models

# Create your models here.
class cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome
