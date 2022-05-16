""" Classe che contiene l'audio di un comando e la relativa traduzione """


class ElementoTradotto:

    def __init__(self, audio, trad):
        self.audio = audio
        self.traduzione = trad
        pass

    def get_audio(self):
        return self.audio

    def get_traduzione(self):
        return self.traduzione
