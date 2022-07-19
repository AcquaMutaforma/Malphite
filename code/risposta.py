"""Classe per racchiudere le info di una risposta, utilizzata dalla classe decisore"""
import json


class Risposta:

    def __init__(self, risposta_dizionario: dict):
        self.idr = risposta_dizionario.get("idr")
        self.nome = risposta_dizionario.get("nome")
        self.registrazione = risposta_dizionario.get("registrazione")
        self.keywords = risposta_dizionario.get("keywords")

    def getjson(self):
        """Ritorna l'oggetto in formato json. Utilizzato per scrivere e leggere
        gli oggetti da/in files locali"""
        return json.dumps(self.__dict__)

