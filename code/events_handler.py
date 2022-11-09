"""
Questo Modulo viene inserito nel framework DJANGO, una volta attivato avvia anche questo.

La sveglia si resetta ogni volta che si spegne?

La sveglia per inserirla con un senso nel DB forse e' divisa per giorno (lun, mar, mer ..) in questo caso
va aggiornato il codice, dovro usare un dizionario { "lun" -> [schedule obj] }
"""
import schedule
import output_handler as out

STATO_SVEGLIA = False
EVENTO_SVEGLIA = None


def suona_sveglia():
    global STATO_SVEGLIA
    if STATO_SVEGLIA:
        out.riproduci_audio('../sveglia.wav')


def set_sveglia(orario: str):
    global EVENTO_SVEGLIA
    EVENTO_SVEGLIA = schedule.every().day.at(orario).do(suona_sveglia())


def sveglia_attiva():
    global STATO_SVEGLIA
    STATO_SVEGLIA = True


def sveglia_spenta():
    global STATO_SVEGLIA
    STATO_SVEGLIA = False