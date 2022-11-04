"""
Modulo che sostituisce i print() con la scrittura nel file di log.
Con una variabile globale possiamo attivare o disattivare i print() e nel frattempo gli eventi vengono
scritti nel file di log, insieme all'orario dell'evento.
"""
import logging
import datetime

# 10=debug 20=info 30=warning 40=error 50=critical
LIVELLO_OUTPUT = 20
logFileName = 'logfile' + datetime.datetime.now().strftime('_%d_%m_%Y') + '.txt'

logging.basicConfig(filename=logFileName, encoding='utf-8',
                    format='[[%(levelname)s]] -- %(asctime)s -- %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=LIVELLO_OUTPUT)


def logInfo(stringa: str):
    logging.info(stringa)


def logWarning(stringa: str):
    logging.warning(stringa)


def logError(stringa: str):
    logging.error(stringa)


def logCritical(stringa: str):
    logging.critical(stringa)
