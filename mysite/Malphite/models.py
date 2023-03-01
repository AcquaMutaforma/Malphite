from django.db import models


# Create your models here.
class Settings(models.Model):
    idS = models.BigAutoField(primary_key=True)
    Alarm = models.TimeField()
    codiceUserTelegram = models.CharField(max_length=9)


class Risposta(models.Model):
    def __str__(self):  # Per i test questo metodo consente di visualizzare l'oggetto invece del suo id a runtime
        return self.nome
    idr = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    percorsoFile = models.CharField(max_length=150)


class Keyword(models.Model):
    # idRisposta = models.ForeignKey(Risposta, on_delete=models.CASCADE)
    # Non sono sicuro di usare questo perche' ho piu risposte per ogni keyword
    id = models.BigAutoField(primary_key=True)
    keyword = models.CharField(max_length=150)
    idRisposta = models.ManyToManyField(Risposta)
