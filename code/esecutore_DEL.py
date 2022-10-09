"""Modulo che esegue le azioni richieste dal decisore. Utilizza 2 moduli,
uno per l'invio delle richieste (audio e testo) tramite messaggistica
e l'altro per la riproduzione di una risposta pre-registrata in formato audi
import elementoTradotto

'''NOTA: questo probabilmente non deve essere una classe, per ora lo lascio cosi'''


class Esecutore:  # utilizzando la classe non dobbiamo scrivere "import"--> si modifica + facilmente dal main

    def __init__(self, messaggistica, output):
        self.mess_h = messaggistica
        self.out_h = output

    def richiesta_non_gestita(self, elem_trad: elementoTradotto.ElementoTradotto):
        Riceve un elem_trad che viene elaborato e inviato tramite mess_h
        self.mess_h.invia_richiesta(elem_trad)

    def esegui_operazione(self, registrazione: str ):
        Da elemento tradotto prendo la traduzione, poi con il filename_risposta l'output handler
        si occupa di recuperare la registrazione da riprodurre.
        self.out_h.riproduci_audio(registrazione)
"""