import elementoTradotto


class Traduttore:
    """ Classe che utilizza un oggetto API per tradurre un audio in testo
    Responsabilita' :
    Viene richiamato da main o audioHandler   #todo: decidere chi
    Utilizza un oggetto apiDiAppoggio per creare un oggetto elementoTradotto
    """

    def __init__(self, api):
        self.api = api
        pass

    def traduci(self, audio):
        testo = self.api.traduzione(audio)
        if testo is not None:
            return elementoTradotto.ElementoTradotto(audio=audio, trad=testo)
        else:
            print("[Traduttore]: traduzione non riuscita, testo = None")
