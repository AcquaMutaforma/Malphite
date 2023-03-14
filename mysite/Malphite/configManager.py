import json
from . import logManager as log

pathConfig = "Malphite/config.txt"


def __leggi_config() -> {}:
    # todo: inserire un controllo sulla correttezza dei dati
    try:
        f = open(pathConfig, 'r')
        to_ret = json.load(f)
        f.close()
        return to_ret
    except FileNotFoundError:
        log.logError("Configurazione non trovata, generata la default")
        f = open(pathConfig, 'w')
        default_config = {
            'api_key': '',
            'user_id': '',
            'stato_sveglia': False,
            'orario_sveglia': '10:00'}
        f.write(json.dumps(default_config))
        f.close()
        return default_config


CONFIG = __leggi_config()


def scrivi_config():
    f = open(pathConfig, 'w')
    f.write(json.dumps(CONFIG))
    f.close()


def get_apiKey() -> str:
    return CONFIG['api_key']


def get_userId() -> str:
    return CONFIG['user_id']


def get_statoSveglia() -> bool:
    return CONFIG['stato_sveglia']


def get_orarioSveglia() -> str:
    return CONFIG['orario_sveglia']


def set_userId(usrid: str):
    try:
        if len(usrid) < 9:
            log.logDebug('USER ID < 9 !!')
        else:
            CONFIG['user_id'] = usrid
            scrivi_config()
            log.logDebug(f"Nuovo User id => [ {usrid} ]")
    except Exception as e:
        log.logError("Errore nel formato User ID per telegram")



def sveglia_attiva():
    CONFIG['stato_sveglia'] = True
    scrivi_config()


def sveglia_spenta():
    CONFIG['stato_sveglia'] = False
    scrivi_config()


def set_orario_sveglia(orario: str):
    if len(orario) != 5:
        pass
    CONFIG['orario_sveglia'] = orario
    scrivi_config()
