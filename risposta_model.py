"""Classe per racchiudere le info di una risposta, utilizzata dalla classe decisore"""
from django.db import models


class Risposta(models.Model):
    idr = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    percorsoFile = models.CharField(max_length=150)


class Keyword(models.Model):
    id = models.BigAutoField(primary_key=True)
    keyword = models.CharField(max_length=150)
    idRisposta = models.ManyToManyField(Risposta)
