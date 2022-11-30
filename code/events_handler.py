"""
Questo Modulo viene inserito nel framework DJANGO, una volta attivato avvia anche questo.
"""
import schedule
import output_handler as out
import file_handler as fh


def crea_sveglia(orario: str):
    return schedule.every().day.at(orario).do(__suona_sveglia())


configurazione = fh.leggi_config()
STATO_SVEGLIA = False
EVENTO_SVEGLIA = None
if configurazione is not None:
    STATO_SVEGLIA = configurazione['stato_sveglia']
    EVENTO_SVEGLIA = crea_sveglia(configurazione['orario_sveglia'])


def __suona_sveglia():
    global STATO_SVEGLIA
    if STATO_SVEGLIA:
        out.riproduci_audio('../sveglia.wav')


def sveglia_attiva():
    global STATO_SVEGLIA
    STATO_SVEGLIA = True


def sveglia_spenta():
    global STATO_SVEGLIA
    STATO_SVEGLIA = False