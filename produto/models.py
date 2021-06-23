from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=19, decimal_places=10)
    marca = models.CharField(max_length=200)
    descricao = models.TextField()
