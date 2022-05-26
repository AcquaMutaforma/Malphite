"""Questo modulo si occupa di definire le azioni da prendere, in base
al comando ricevuto in formato {elementoTradotto}. Contiene una lista di
parole chiave associate ad un risposta, e una lista di appoggio per
valutare la risposta piu' corretta. """
import elementoTradotto
import fileHandler
import risposta

mappa_logica = []
mappa_valutazione = []


def valuta_comando(elem_trad):
    pass  # todo


def load_mappa():
    f"""Carica la mappa da un file, recuperato tramite fileHandler.
    Inizializza la {mappa_valutazione} con gli oggetti risposta, mentre inizializza
    la {mappa_logica} con le parole chiave relative alle risposte."""
    pass  # todo


def add_risposta():
    """Aggiunge una nuova risposta alla tabella, e richiede a fileHandler
    di modificare il file della mappa."""
    pass  # todo


def rm_risposta():
    """Se presente, rimuove una nuova risposta dalla tabella, e richiede a fileHandler
        di modificare il file della mappa."""
    pass  # todo


def __init__():
    load_mappa()
    pass
