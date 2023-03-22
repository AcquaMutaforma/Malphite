import schedule
from . import logManager as log
from . import output_handler as out
from . import configManager as conf

STATO_SVEGLIA = conf.get_statoSveglia()
ORARIO_SVEGLIA = conf.get_orarioSveglia()


def suona_sveglia():
    global STATO_SVEGLIA
    if STATO_SVEGLIA:
        out.suonaSveglia()


def __crea_sveglia(orario: str):
    # Formato = hh:mm, il default del file config e' 10:00
    try:
        toret = schedule.every().day.at(orario).do(lambda: suona_sveglia())
        log.logDebug(f"Creata sveglia per le {orario}")
        return toret
    except TypeError as e:
        log.logError(f"Errore creazione sveglia {e}")
        return None


EVENTO_SVEGLIA = __crea_sveglia(ORARIO_SVEGLIA)


def sveglia_attiva():
    global STATO_SVEGLIA
    conf.sveglia_attiva()
    STATO_SVEGLIA = True


def sveglia_spenta():
    global STATO_SVEGLIA
    conf.sveglia_spenta()
    STATO_SVEGLIA = False


def modificaSveglia(orario: str):
    global EVENTO_SVEGLIA, ORARIO_SVEGLIA
    conf.set_orario_sveglia(orario)
    ORARIO_SVEGLIA = orario
    tmp = __crea_sveglia(orario)
    if tmp is not None:
        EVENTO_SVEGLIA = tmp

