import schedule
import output_handler as out
import configManager as conf


def __crea_sveglia(orario: str):
    # Formato = hh:mm, il default del file config e' 10:00
    return schedule.every().day.at(orario).do(__suona_sveglia())


STATO_SVEGLIA = conf.get_statoSveglia()
ORARIO_SVEGLIA = conf.get_orarioSveglia()
EVENTO_SVEGLIA = __crea_sveglia(ORARIO_SVEGLIA)


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


def modificaSveglia(orario: str):
    global EVENTO_SVEGLIA
    #todo : aggiungere la modifica nella config x tutte le funzioni
    EVENTO_SVEGLIA = __crea_sveglia(orario)
