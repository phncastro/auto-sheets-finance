from django.db import models

class Transacao(models.Model):
    
    id = models.AutoField(primary_key=True, auto_created=True)
    tipo = models.CharField(max_length=100)
    valor = models.FloatField(null=False)
    descricao = models.CharField(max_length=200, null=False)
    banco = models.CharField(max_length=100)