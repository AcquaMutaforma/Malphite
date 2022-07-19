"""Modulo che esegue le azioni richieste dal decisore. Utilizza 2 moduli,
uno per l'invio delle richieste (audio e testo) tramite messaggistica
e l'altro per la riproduzione di una risposta pre-registrata in formato audio"""
import elementoTradotto

"""Nota
L'oggetto message_handler che contiene i dati per l'invio di telegram andrebbe tenuto qua,
si potrebbe creare non all'inizializzazione (__init__) ma quando viene richiesto la prima volta,
cosi se non serve proprio, non viene creato -A-"""


class Esecutore:  # utilizzando la classe non dobbiamo scrivere "import" quindi si modifica + facilmente dal main

    def __init__(self, messaggistica, output):
        self.mess_h = messaggistica
        self.out_h = output

    def richiesta_non_gestita(self, elem_tradotto: elementoTradotto):
        """Riceve un elem_trad che viene elaborato e inviato tramite mess_h"""
        self.mess_h.invia_richiesta(elem_tradotto)

    def esegui_operazione(self, filename_risposta: str):
        """Da elemento tradotto prendo la traduzione, poi con il filename_risposta l'output handler
        si occupa di recuperare la registrazione da riprodurre."""
        self.out_h.riproduci_audio(filename_risposta)

