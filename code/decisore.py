"""Questo modulo si occupa di definire le azioni da prendere, in base
al comando ricevuto in formato {elementoTradotto}. Contiene una lista di
parole chiave associate ad un risposta, e una lista di appoggio per
valutare la risposta piu' corretta. """
import elementoTradotto
import fileHandler

mappa_logica = []
mappa_valutazione = []


def valuta_comando(elem_trad):
    pass


def load_mappa():
    """Carica la mappa da un file, recuperato tramite fileHandler"""
    pass


def add_risposta():
    """Aggiunge una nuova risposta alla tabella, e richiede a fileHandler
    di modificare il file della mappa."""
    pass


def rm_risposta():
    """Se presente, rimuove una nuova risposta dalla tabella, e richiede a fileHandler
        di modificare il file della mappa."""
    pass


def __init__():
    load_mappa()
    pass
