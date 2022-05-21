"""Modulo che esegue le azioni richieste dal decisore. Utilizza 2 moduli,
uno per l'invio delle richieste (audio e testo) tramite messaggistica
e l'altro per la riproduzione di una risposta pre-registrata in formato audio"""


class Esecutore:  # utilizzando la classe non dobbiamo scrivere "import" quindi si modifica dal main

    def __init__(self, messaggistica, output):
        self.mess_h = messaggistica
        self.out_h = output

    def richiesta_non_gestita(self, id_risp):
        """Riceve un elem_trad che viene elaborato e inviato tramite mess_h"""

