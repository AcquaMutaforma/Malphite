import elementoTradotto


class Traduttore:
    """ Classe che utilizza un oggetto API per tradurre un audio in testo
    Responsabilita' :
    Viene richiamato da main o audioHandler   #todo: decidere chi
    Utilizza un oggetto apiDiAppoggio per creare un oggetto elementoTradotto
    """

    def __init__(self, api):
        self.api = api
        print("[Traduttore] Pronto")
        pass

    def traduci(self, audio):
        testo = self.api.traduzione(audio)
        print(f"[Traduttore] Testo = {testo}")
        if testo is not None:
            return elementoTradotto.ElementoTradotto(audio=audio, trad=testo)
        else:
            print("[Traduttore]: traduzione non riuscita, testo = None")
