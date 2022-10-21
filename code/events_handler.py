import schedule
import backend


STATO_SVEGLIA = False


def suona_sveglia():
    if STATO_SVEGLIA:
        backend.suona_sveglia()


EVENTO_SVEGLIA = schedule.every().day.at('10:00').do(suona_sveglia())


def crea_schedule(orario: str):
    return schedule.every().day.at(orario).do(suona_sveglia())
