""" Classe utilizzata per creare una richiesta alla piattaforma AssemblyAI per
una traduzione Speech to text """
import requests


class servizioAai:
    token = "f89c5a7a9b884ea38b835f621e5e42d4"
    headers = {
        "authorization": token,
        "content-type": "application/json"
    }
    url_traduzione = "https://api.assemblyai.com/v2/transcript"

    def __init__(self):
        pass

    def __leggiFile(self, filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    # invia il file audio alla piattaforma e restituisce il link del file nella piattaforma
    def __upload(self, filename):
        risposta_json = requests.post('https://api.assemblyai.com/v2/upload', headers=self.headers,
                                      data=self.__leggiFile(filename))
        url_file = risposta_json.json()['upload_url']
        audio_url_json = {"audio_url": url_file,
                          "language_code": "it"}

        response = requests.post(self.url_traduzione, json=audio_url_json,
                                 headers=self.headers)
        return response.json()['id']

    # usando l'id fa UNA richiesta alla piattaforma per la traduzione
    def __getTraduzione(self, id):
        traduzione = requests.get(self.url_traduzione + "/" + id, headers=self.headers)
        return traduzione.json()['text']

    def traduzione(self, audio_path):
        id_file = self.__upload(audio_path)
        while 1:
            text = self.__getTraduzione(id_file)
            if text != 'None':
                break
        return text


