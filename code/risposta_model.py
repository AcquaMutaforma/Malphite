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


def get_risposta_by_idr(idrisposta: int) -> Risposta:
    return Risposta.objects.get(idr=idrisposta)


def get_idrisposte_con_keyword(keyword: str) -> tuple[str]:
    return Keyword.objects.values_list('idRisposta')


def aggiungi_risposta_alla_keyword(keyword: str, idRisposta: int):
    lista_oggetti_keyword = Keyword.objects.filter(keyword=keyword)  # il formato e' dictionary
    if len(lista_oggetti_keyword) < 1:
        parola = Keyword.objects.create(keyword=keyword, idRisposta=idRisposta)
        parola.save()
    else:
        for x in lista_oggetti_keyword:
            x.self.idRisposta.append(idRisposta)
            x.save()


def flush_keyword_senza_risposte():
    lista = Keyword.objects.all()
    for x in lista:
        if len(x.idRisposta) == 0:
            x.remove()
