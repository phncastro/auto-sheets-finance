from django.db import models


class Transacao(models.Model):
    
    id = models.AutoField(
        primary_key=True,
        auto_created=True
        )
    data = models.DateField(
        auto_now_add=True
        )
    banco = models.CharField(
        max_length=100
        )
    tipo = models.CharField(
        max_length=100
        )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    descricao = models.CharField(
        max_length=200,
        null=False
        )
    categoria = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )
