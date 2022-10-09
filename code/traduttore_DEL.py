import elementoTradotto


class Traduttore:
    f""" Classe che utilizza un oggetto API per tradurre un audio in testo
    Responsabilita' :
    Viene richiamato dal main
    Utilizza un oggetto apiDiAppoggio per creare un oggetto {elementoTradotto}
    """

    def __init__(self, api):
        self.api = api
        print("[Traduttore] - Pronto")
        pass

    def traduci(self, audio: str):
        """ Metodo che attraverso l'oggetto api che contiene, traduce un audio in testo
        :param audio: path del file audio """
        print("[Traduttore] - avvio API")
        testo = MyAPItraduzione(audio)
        print(f"[Traduttore] - traduzione= {testo}")
        if testo is not None:
            return elementoTradotto.ElementoTradotto(audio=audio, trad=testo)
        else:
            print("[Traduttore] - traduzione non riuscita, testo = None")
            return None
