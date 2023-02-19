import json


def __leggi_config() -> {}:
    # todo: inserire un controllo sulla correttezza dei dati
    try:
        f = open("config.txt", 'r')
        to_ret = json.load(f)
        f.close()
        return to_ret
    except FileNotFoundError:
        f = open("config.txt", 'w')
        f.write(json.dumps({
            'api_key': '',
            'user_id': '',
            'stato_sveglia': False,
            'orario_sveglia': ''}))
        f.close()
    return {
        'api_key': '',
        'user_id': '',
        'stato_sveglia': False,
        'orario_sveglia': ''}


CONFIG = __leggi_config()


def scrivi_config():
    f = open("config.txt", 'w')
    f.write(json.dumps(CONFIG))
    f.close()


def get_apiKey():
    return CONFIG['api_key']


def get_userId():
    return CONFIG['user_id']


def set_userId(usrid: str):
    # todo: aggiungere controlli
    CONFIG['user_id'] = usrid
    scrivi_config()
