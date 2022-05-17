""" Classe utilizzata per creare una richiesta alla piattaforma AssemblyAI per
una traduzione Speech to text """
import requests

token = "f89c5a7a9b884ea38b835f621e5e42d4"
headers = {
    "authorization": token,
    "content-type": "application/json"
}
url_traduzione = "https://api.assemblyai.com/v2/transcript"


def __leggi_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


def __upload(filename):
    """invia il file audio alla piattaforma e restituisce il link del file nella piattaforma"""
    risposta_json = requests.post('https://api.assemblyai.com/v2/upload', headers=headers,
                                  data=__leggi_file(filename))
    # todo: aggiungere controlli dopo le richieste, ad esempio connessione fallita etc o anche try-catch
    url_file = risposta_json.json()['upload_url']
    audio_url_json = {"audio_url": url_file,
                      "language_code": "it"}

    response = requests.post(url_traduzione, json=audio_url_json,
                             headers=headers)
    return response.json()['id']


def __get_traduzione(id_audio):
    """usando l'id fa UNA richiesta alla piattaforma per la traduzione"""
    trad = requests.get(url_traduzione + "/" + id_audio, headers=headers)
    if trad.json()['status'] == "completed":
        return trad.json()['text']
    else:
        return None


def traduzione(audio_path):  # todo mettere un boolean per abilitare i print, aiuta con debug
    id_file = __upload(audio_path)
    print(f"[AAI] audio path = {audio_path} - - ID file = {id_file}")
    nav = 1
    while 1:
        richiesta = __get_traduzione(id_file)
        print(f"[AAI] numero richiesta = {nav} - - richiesta = {richiesta}")
        if richiesta is not None:
            break
        nav += 1
    print(f"[AAI] testo = {richiesta}")
    return richiesta
