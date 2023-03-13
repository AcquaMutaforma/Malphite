from django.db import models


class Settings(models.Model):
    Alarm = models.TimeField()
    codiceUserTelegram = models.CharField(max_length=9, null=True)


class Risposta(models.Model):
    def __str__(self):  # Per i test questo metodo consente di visualizzare l'oggetto invece del suo id a runtime
        return self.nome
    idr = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    percorsoFile = models.CharField(max_length=150)


class Keyword(models.Model):
    # idRisposta = models.ForeignKey(Risposta, on_delete=models.CASCADE)
    # Non sono sicuro di usare questo perche' ho piu risposte per ogni keyword
    def __str__(self):  # Per i test questo metodo consente di visualizzare l'oggetto invece del suo id a runtime
        return self.keyword
    id = models.BigAutoField(primary_key=True)
    keyword = models.CharField(max_length=150)


class Relazione(models.Model):
    idRisposta = models.ForeignKey(Risposta, on_delete=models.CASCADE)
    idKeyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
