from django.db import models

class Transaction(models.Model):
    texto = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)