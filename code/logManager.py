"""
Modulo che sostituisce i print() con la scrittura nel file di log.
Con una variabile globale possiamo attivare o disattivare i print() e nel frattempo gli eventi vengono
scritti nel file di log, insieme all'orario dell'evento.
"""
import logging
import datetime

# 10=debug 20=info 30=warning 40=error 50=critical
LIVELLO_OUTPUT = 10
logFileName = 'logfile' + datetime.datetime.now().strftime('_%d_%m_%y') + '.txt'

logging.basicConfig(filename=logFileName, encoding='utf-8',
                    format='[[%(levelname)s]] - %(asctime)s - %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p',
                    level=LIVELLO_OUTPUT)


def logDebug(stringa: str):
    logging.debug(stringa)


def logInfo(stringa: str):
    logging.info(stringa)


def logWarning(stringa: str):
    print(str)
    logging.warning(stringa)


def logError(stringa: str):
    print(str)
    logging.error(stringa)


def logCritical(stringa: str):
    print(str)
    logging.critical(stringa)
