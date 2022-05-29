"""Questo modulo si occupa di definire le azioni da prendere, in base
al comando ricevuto in formato {elementoTradotto}. Contiene una lista di
parole chiave associate ad un risposta, e una lista di appoggio per
valutare la risposta piu' corretta. """
import json
import esecutore
import elementoTradotto
import file_handler
import risposta


class Decisore:

    def __init__(self, esec: esecutore):
        self.mappa_logica = {}  # mappa con keywords -> id_risposta
        self.mappa_valutazione = {}  # mappa con obj_risposta -> N (punteggio per keywords corrispondenti alla risposta)
        self.esecutore = esec
        self.load_mappa()

    def valuta_comando(self, elem_trad: elementoTradotto):
        f"""
    - controllo se e' presente una traduzione
    - con filtra_richiesta(elem_trad.traduzione) filtro la traduzione di {elem_trad} e ritorno una lista
    - per ogni parola nella lista, se e' presente nella {self.mappa_logica}, allora 
    incremento il valore nella {self.mappa_valutazione}
    - finita la lista, valuto la {self.mappa_valutazione}, se abbiamo un numero maggiore allora mando a esecutore,
    idem se abbiamo parita' o non trova riscontri nelle keywords
    - resetta mappa valutazione. 
    - infine, se non viene inviato al mess_handler elimina il file audio.
        """
        pass  # todo

    def load_mappa(self):
        f"""Carica la mappa da un file, recuperato tramite fileHandler.
        Inizializza la {self.mappa_valutazione} con gli oggetti risposta, mentre inizializza
        la {self.mappa_logica} con le parole chiave relative alle risposte."""
        lista = json.load(file_handler.get_mappa_decisore())
        for i in lista:
            # todo: aggiungere controlli
            risp = risposta.Risposta(i['id'], i['nome'], i['registrazione'], i['keywords'])
            for k in risp.keywords:
                self.mappa_logica[str(k).lower()] = str(risp.id_risp)
                # se e' gia presente una keyword? modifichiamo il valore (id) in una lista di id (?)idk
            self.mappa_valutazione[risp.id_risp] = 0

    def add_risposta(self):
        """Aggiunge una nuova risposta alla tabella, e richiede a fileHandler
        di modificare il file della mappa."""
        pass  # todo

    def rm_risposta(self):
        """Se presente, rimuove una nuova risposta dalla tabella, e richiede a fileHandler
            di modificare il file della mappa."""
        pass  # todo

    def reset_mappa_valutazione(self):
        for x in self.mappa_valutazione.keys():
            self.mappa_valutazione[x] = 0


def filtra_richiesta(string: str):
    """Metodo che sottrae le parole piu' corte di 3 caratteri e ritorna una lista
            con le parole presenti nel comando ricevuto"""
    pass  # todo
