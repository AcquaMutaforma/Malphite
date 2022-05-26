"""Classe per racchiudere le info di una risposta, utilizzata dalla classe decisore"""
import json


class Risposta:
    def __init__(self, nome, registrazione, parole_chiave):
        self.nome = nome
        self.registrazione = registrazione
        self.parolechiave = parole_chiave

    def getjson(self):
        """Ritorna l'oggetto in formato json. Utilizzato per scrivere e leggere
        gli oggetti da/in files locali"""
        return json.dumps({
            "nome": self.nome,
            "registrazone": self.registrazione,
            "keywords": self.parolechiave
        })

