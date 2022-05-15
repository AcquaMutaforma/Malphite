import requests

filename = "C:\\Users\\Aley\\Desktop\\Registrazione.m4a"
token = "f89c5a7a9b884ea38b835f621e5e42d4"


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


def traduci_audio():
    headers = {'authorization': token,
                   "content-type": "application/json"}
    risposta_json = requests.post('https://api.assemblyai.com/v2/upload', headers=headers,
                                  data=read_file(filename))

    print("--------- risposta 1---------")
    print(risposta_json.json())
    print("--------- fine risposta 1---------")
    # todo sono arrivato qua -----------------------------------------------
    url_traduzione = "https://api.assemblyai.com/v2/transcript"
    audio_url_json = {"audio_url": risposta_json.json()['upload_url'],
                      "language_code": "it"}

    response = requests.post(url_traduzione, json=audio_url_json, headers=headers)
    print("--------- risposta 2---------")
    print(response.json())
    print("--------- fine risposta 2---------")
    print("ID == " + response.json()['id'])

    print("url == " + url_traduzione + "/" + response.json()['id'])
    traduzione = ''
    nav = 0
    while 1:
        traduzione = requests.get(url_traduzione + "/" + response.json()['id'], headers=headers)
        print("--------- risposta " + str(nav) + " ---------")
        print(traduzione.json())
        print("--------- fine risposta " + str(nav) + " ---------")
        if traduzione.json()['status'] == "completed":
            break
        nav += 1

    print("\nTesto audio = " + traduzione.json()['text'])
