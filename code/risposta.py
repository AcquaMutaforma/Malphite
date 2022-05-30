"""Classe per racchiudere le info di una risposta, utilizzata dalla classe decisore"""
import json


class Risposta:

    def __init__(self, diz: dict):
        self.idr = diz.get("idr")
        self.nome = diz.get("nome")
        self.registrazione = diz.get("registrazione")
        self.keywords = diz.get("keywords")

    def getjson(self):
        """Ritorna l'oggetto in formato json. Utilizzato per scrivere e leggere
        gli oggetti da/in files locali"""
        return json.dumps(self.__dict__)

