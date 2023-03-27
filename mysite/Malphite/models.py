from django.db import models


class Settings(models.Model):
    Alarm = models.TimeField()
    codiceUserTelegram = models.CharField(max_length=9, null=True)


class Risposta(models.Model):
    def __str__(self):
        return self.nome
    idr = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    percorsoFile = models.CharField(max_length=150)


class Keyword(models.Model):
    def __str__(self):
        return self.keyword
    id = models.BigAutoField(primary_key=True)
    keyword = models.CharField(max_length=150)


class Relazione(models.Model):
    idRisposta = models.ForeignKey(Risposta, on_delete=models.CASCADE)
    idKeyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
