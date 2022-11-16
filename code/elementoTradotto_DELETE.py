""" Classe che contiene l'audio di un comando e la relativa traduzione """


class ElementoTradotto:

    def __init__(self, file_audio: str, trad: str):
        self.file_audio = file_audio
        self.traduzione = trad
        print(f"[EleTradotto] - new - - audio= {self.file_audio} - - traduzione= {self.traduzione}")
