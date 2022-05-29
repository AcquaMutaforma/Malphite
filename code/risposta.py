"""Classe per racchiudere le info di una risposta, utilizzata dalla classe decisore"""
import json


class Risposta:
    def __init__(self, id_risp, nome, file_registrazione, parole_chiave):
        self.id_risp = id_risp
        self.nome = nome
        self.registrazione = file_registrazione
        self.keywords = parole_chiave

    def getjson(self):
        """Ritorna l'oggetto in formato json. Utilizzato per scrivere e leggere
        gli oggetti da/in files locali"""
        return json.dumps({
            'nome': self.nome,
            'registrazone': self.registrazione,
            'keywords': self.keywords
        })

